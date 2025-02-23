# nl2sql - Natural Language to SQL Query Converter

## Overview

`nl2sql` is a project that translates natural language questions into SQL queries. It aims to provide a user-friendly interface for interacting with databases, enabling users with limited SQL knowledge to retrieve information efficiently.

## Features

*   **Natural Language to SQL Conversion:** Converts user-provided natural language questions into executable SQL queries.
*   **Database Interaction:** Executes generated SQL queries against a configured database and returns the results.
*   **User Interface:** Provides a web-based interface for users to input questions and view results.
*   **LLM Integration:** Leverages a Generative Model (like Gemini) to understand natural language and generate SQL.
*   **Customizable Prompts:** Allows customization of prompts to guide the LLM for better SQL generation.
*   **Error Handling:** Includes mechanisms for correcting invalid SQL queries.
*   **Pagination:** Implements pagination for handling large query results.
*   **Horizontal Scrolling:** Provides horizontal scrolling for tables that overflow their containers.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd nl2sql
    ```

3.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\\Scripts\\activate  # On Windows
    ```

4.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up environment variables:**

    *   Create a [.env](http://_vscodecontentref_/18) file in the project root.
    *   Add the following variables, replacing the placeholders with your actual values:

        ```
        GOOGLE_API_KEY=<your_google_api_key>
        DB_PASS=<your_database_password>
        DATABASE=<your_database_name>
        USER=<your_database_user>
        HOST=<your_database_host>
        DATABASE_CLIENT=<your_database_client, e.g., postgresql>
        PORT=<your_database_port>
        ```

## Configuration

*   **Database Configuration:**  The database connection details are configured using environment variables (see Installation).
*   **LLM Configuration:** The LLM model name (e.g., `"gemini-2.0-flash"`) and system instruction are configured in the [llm.py](http://_vscodecontentref_/19) file.  You can also adjust the [generation_config](http://_vscodecontentref_/20) to control the LLM's behavior (e.g., `response_mime_type`).
*   **Prompts:**  SQL generation prompts are stored in [prompts.py](http://_vscodecontentref_/21) and can be customized to improve SQL generation accuracy.

## Usage

1.  **Run the FastAPI application:**

    ```bash
    python src/server/app.py
    ```

2.  **Open the application in your web browser:**

    *   Navigate to `http://localhost:8000` (or the appropriate address if you've configured a different port).

3.  **Enter your natural language question in the chat input.**

4.  **View the generated SQL query and the query results in the chat area.**

## Key Components

*   **[src/server/app.py](http://_vscodecontentref_/22):**  The main FastAPI application.  Handles routing, request processing, and rendering of responses.
*   **[src/server/core/llm.py](http://_vscodecontentref_/23):**  Wraps the Generative Model (e.g., Gemini) and provides methods for generating SQL queries from natural language.
*   **[src/utils/database_utils.py](http://_vscodecontentref_/24):**  Handles database connections and query execution.
*   **[src/utils/prompts.py](http://_vscodecontentref_/25):**  Contains prompts used to guide the LLM in generating SQL queries.
*   **[src/server/templates/chat_response.html](http://_vscodecontentref_/26):** Jinja2 template for rendering the chat interface, including the user query, SQL query, and table results.
*   **[src/static/style.css](http://_vscodecontentref_/27):** CSS stylesheet for the application's appearance.

## Working Incrementally

The project is structured to allow for incremental development and experimentation:

*   **Notebooks:** Use the Jupyter notebooks in the [notebooks](http://_vscodecontentref_/28) directory to experiment with different prompts, LLM configurations, and data analysis techniques.
*   **Modular Design:** The separation of concerns into modules (e.g., [llm.py](http://_vscodecontentref_/29), [database_utils.py](http://_vscodecontentref_/30)) makes it easier to modify and test individual components.
*   **Configuration:** Externalize configuration settings (API keys, database credentials) using environment variables to avoid hardcoding sensitive information.

## Datasets

The [data](http://_vscodecontentref_/31) directory contains sample datasets related to airlines, airports, and flights. These datasets can be used for testing and demonstration purposes.

## Project Structure

```
.
├── .env
├── .gitignore
├── Dockerfile
├── [README.md](http://_vscodecontentref_/32)
├── [requirements.txt](http://_vscodecontentref_/33)
├── data
│   ├── airlines.csv
│   ├── airports.csv
│   ├── eval.csv
│   └── flights.csv
├── docs
├── notebooks
│   ├── [airline_dataset.ipynb](http://_vscodecontentref_/34)
│   ├── [data.ipynb](http://_vscodecontentref_/35)
│   ├── [data_engineering.ipynb](http://_vscodecontentref_/36)
│   ├── [eval.ipynb](http://_vscodecontentref_/37)
│   ├── exp copy.ipynb
│   ├── [exp.ipynb](http://_vscodecontentref_/38)
│   ├── [llm_evaluation.ipynb](http://_vscodecontentref_/39)
│   └── [llm_retrying.ipynb](http://_vscodecontentref_/40)
├── package.json
├── src
│   ├── [__init__.py](http://_vscodecontentref_/41)
│   ├── config
│   │   ├── [__init__.py](http://_vscodecontentref_/42)
│   │   └── config.py
│   ├── db
│   │   ├── [__init__.py](http://_vscodecontentref_/43)
│   │   └── database.py
│   ├── server
│   │   ├── [__init__.py](http://_vscodecontentref_/44)
│   │   ├── [app.py](http://_vscodecontentref_/45)
│   │   ├── core
│   │   │   └── llm.py
│   │   └── templates
│   ├── static
│   │   └── [style.css](http://_vscodecontentref_/46)
│   ├── tests
│   └── utils
│       ├── [__init__.py](http://_vscodecontentref_/47)
│       ├── common_utils.py
│       ├── database_utils.py
│       └── prompts.py
└── templates
```

## Contributing

Contributions are welcome!  Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write unit tests to verify your changes.
5.  Submit a pull request.

## License

[Specify the license for your project]