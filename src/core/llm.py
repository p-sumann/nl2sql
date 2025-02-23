from typing import TypedDict

import google.generativeai as genai

from src.utils.prompts import sql_generation_system_prompt


class SQL(TypedDict):
    results: str


class GenerativeModelWrapper:
    def __init__(self, model_name: str = "gemini-2.0-flash"):
        self.model = genai.GenerativeModel(
            model_name=model_name, system_instruction=sql_generation_system_prompt
        )

    async def generate_sql(self, prompt: str) -> SQL:
        result = await self.model.generate_content_async(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                response_schema={
                    "type": "object",
                    "properties": {"sql": {"type": "string"}},
                    "required": ["sql"],
                },
            ),
            request_options={"timeout": 600},
        )
        return result.text
