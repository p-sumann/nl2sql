# Text-to-SQL

## Overview

`Text-to-SQL` is a project that translates natural language questions into SQL queries. It aims to provide a user-friendly interface for interacting with databases, enabling users with limited SQL knowledge to retrieve information efficiently.

## Features

*   **Natural Language to SQL Conversion:** Converts user-provided natural language questions into executable SQL queries.
*   **Database Interaction:** Executes generated SQL queries against a configured database and returns the results.
*   **User Interface:** Provides a web-based interface for users to input questions and view results.
*   **LLM Integration:** Leverages Google's Gemini model to understand natural language and generate SQL.
*   **Customizable Prompts:** Allows customization of prompts to guide the LLM for better SQL generation.
*   **Error Handling:** Includes mechanisms for correcting invalid SQL queries.
*   **Modular Architecture:** Clean separation of concerns for easy maintenance and extensibility.
*   **Comprehensive Testing:** Includes unit tests and integration tests.
*   **Development Tools:** Jupyter notebooks for experimentation and analysis.

## Prerequisites

*   Python 3.8 or higher
*   PostgreSQL 12 or higher
*   Google API key for Gemini model access
*   Git (for cloning the repository)
*   Linux/macOS Systems

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/p-sumann/nl2sql
    cd nl2sql
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Create environment file:**

    Create a `.env` file in the project root with the following variables: sample keys used in this project are provided except for Google.

    ```bash
    touch .env
    ```

    ```
    GOOGLE_API_KEY=<your_google_api_key>
    DB_PASS=<your pass> #postgres
    DATABASE=<your db> #text2sql
    USER=<your user> #postgres
    HOST=<your host> #localhost
    DATABASE_CLIENT=<your db client> #postgresql
    PORT=<your port> #5432
    ```

2.  **LLM Configuration:**

    - Model settings can be adjusted in `src/core/llm.py`
    - Default model: `gemini-2.0-flash`
    - Customize generation parameters in the `GenerativeModelWrapper` class

3.  **Database Configuration:**

    - Connection settings are managed through environment variables
    - Default database name: `text2sql`
    - Default user: `postgres`



## Database Setup

For, this demo purpose, the default user and password is used, for production use, use safe values and use environment variables in bash script.

1.  **Install and Initialize the database:**

    ```bash
    # Run the database initialization script
    cd src/db
    chmod +x init.sh
    ./init.sh
    ```

3.  **Create database tables:**

    ```bash
    cd .. ..
    python src/db/create_table.py
    ```

4.  **Load sample data:**

    ```bash
    python src/db/load_data.py
    ```

## Running the Application

1.  **Start the FastAPI server:**

    ```bash
    python src/server/app.py
    ```

2.  **Access the web interface:**

    - Open your browser and navigate to `http://localhost:8000`
    - Enter natural language questions in the chat input
    - View generated SQL queries and results

## Project Structure
### Root Directory
- `.env`: Environment variables configuration
- `.gitignore`: Git ignore file
- `Dockerfile`: Docker container configuration
- `requirements.txt`: Python dependencies

### Data (/data)
Contains CSV files with flight-related information:
- `airlines.csv`: Airline company data
- `airports.csv`: Airport information
- `flights.csv`: Flight records
- `eval.csv`: Evaluation dataset

### Notebooks (/notebooks)
Jupyter notebooks for development and testing:
- `airline_dataset.ipynb`: Dataset analysis
- `eval.ipynb`: Evaluation scripts
- `initial_exp.ipynb`: Initial experiments
- `llm_retrying.ipynb`: LLM retry logic tests

### Source Code (/src)
Main application code:
- `config/`: Configuration settings
- `db/`: Database operations and initialization
- `server/`: Web server implementation
    - `core/llm.py`: LLM integration
    - `templates/`: Server-side templates
- `static/`: CSS styles
- `tests/`: Unit and integration tests
- `utils/`: Utility functions
    - `common_utils.py`: Common helper functions
    - `database_utils.py`: Database utilities
    - `prompts.py`: LLM prompt templates

### Templates
Frontend templates:
- `chat_response.html`: Chat interface
- `index.html`: Main page
- `static/style.css`: CSS styling

## Project Tree

```
.
├── .env
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── data
│   ├── airlines.csv
│   ├── airports.csv
│   ├── eval.csv
│   └── flights.csv
├── notebooks
│   ├── airline_dataset.ipynb
│   ├── eval.ipynb
│   ├── initial_exp.ipynb
│   └── llm_retrying.ipynb
├── src
│   ├── __init__.py
│   ├── config                          #config module
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db                              #database module
│   │   ├── __init__.py
│   │   └── database.py
│   │   └── create_table.py
│   │   └── database.py
│   │   └── load_data.py
│   │   └── init.sh
│   ├── server                          #core fastapi app
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── core
│   │   │   └── llm.py
│   │   └── templates
│   ├── tests                           #tests modules
│   │   ├── __init__.py
│   │   └── conftest.py
│   │   └── test_database.py
│   │   └── test_query.py
│   └── utils                           #utility module
│       ├── __init__.py
│       ├── common_utils.py
│       ├── database_utils.py
│       └── prompts.py
└── templates                           #html  templates
│   └── chat_response.html
│   └── index.html
├── static                              #UI styling
│   └── style.css
```


## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.