import json
import logging
import os
import sys
from typing import Dict, Tuple

import markdown2
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.core.llm import GenerativeModelWrapper
from src.utils.common_utils import clean_generation_result
from src.utils.database_utils import DatabaseConnector
from src.utils.prompts import sql_correction_prompt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="src/server/templates/")
templates.env.filters["markdown"] = markdown2.markdown
app.mount("/static", StaticFiles(directory="src/server/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database connector
db_connector = DatabaseConnector()


async def generate_sql(
    user_query: str, llm: GenerativeModelWrapper, prompt: str = None
) -> str:
    """Generates SQL query using the LLM."""
    try:
        response = await llm.generate_sql(prompt or user_query)
        cleaned_response = clean_generation_result(response)
        parsed = json.loads(cleaned_response)
        generated_sql = parsed.get("sql", "")
        return generated_sql
    except (json.JSONDecodeError, KeyError) as e:
        logger.error(f"LLM response parsing error: {e}")
        raise HTTPException(status_code=500, detail="Failed to parse LLM response.")
    except Exception:
        logger.exception("Unexpected error during SQL generation")
        raise HTTPException(status_code=500, detail="Error generating SQL.")


async def generate_and_execute_with_retries(user_query: str) -> Tuple[str, Dict]:
    """
    Attempts to generate a corrected SQL query and execute it up to 3 times.
    If all attempts fail, an HTTPException is raised.
    Returns a tuple of (corrected SQL query string, query results).
    """
    max_attempts = 3
    attempt = 0
    error_message = ""
    generated_sql = ""

    llm = GenerativeModelWrapper()

    while attempt < max_attempts:
        attempt += 1
        try:
            logger.info("Generating SQL")
            if attempt == 1:
                generated_sql = await generate_sql(user_query, llm)
            else:
                prompt = sql_correction_prompt.format(
                    user_query=user_query,
                    generated_sql=generated_sql,
                    error_message=error_message,
                )
                generated_sql = await generate_sql(user_query, llm, prompt)
            logger.info("Executing SQL")
            results = db_connector.execute_query(generated_sql)
            logger.info(f"Attempt {attempt}: Query executed successfully.")
            return generated_sql, results

        except HTTPException as http_ex:
            error_message = http_ex.detail
            logger.warning(f"Attempt {attempt} failed: {error_message}")
        except Exception as e:
            error_message = str(e)
            logger.exception(f"Attempt {attempt} failed with unexpected error")

    logger.error("SQL query execution failed after 3 attempts.")
    raise HTTPException(
        status_code=500, detail="SQL query execution failed after 3 attempts."
    )


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, text: str = Form(...)):
    """Handles chat requests, generates SQL, executes it, and returns the results."""
    try:
        user_query = text

        if not user_query.strip():
            return templates.TemplateResponse(
                "chat_response.html",
                {
                    "request": request,
                    "results": [],
                    "text": user_query,
                    "sql": "No query entered.",
                },
            )
        logger.info(f"User Query: {user_query}")
        logger.info("Invoking LLM")

        sql, results = await generate_and_execute_with_retries(user_query)

        if not results:
            return templates.TemplateResponse(
                "chat_response.html",
                {
                    "request": request,
                    "results": [],
                    "text": user_query,
                    "sql": sql,
                    "error_message": "No results found for this query.",
                },
            )

        return templates.TemplateResponse(
            "chat_response.html",
            {
                "request": request,
                "results": results,
                "text": user_query,
                "sql": f"{sql};",
            },
        )

    except HTTPException as http_ex:
        # Handle exceptions raised during SQL generation or execution
        return templates.TemplateResponse(
            "chat_response.html",
            {
                "request": request,
                "results": [],
                "text": text,
                "sql": "",
                "error_message": http_ex.detail,
            },
        )
    except Exception as e:
        # Handle unexpected exceptions
        error_message = "An unexpected error occurred while processing your request. Please try again later."
        logger.exception(f"Unexpected error: {e}")
        return templates.TemplateResponse(
            "chat_response.html",
            {
                "request": request,
                "results": [],
                "text": text,
                "sql": "",
                "error_message": error_message,
            },
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
