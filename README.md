# nl2sql

## Overview

`nl2sql` is a project that converts natural language queries into SQL queries. This project aims to bridge the gap between non-technical users and databases by allowing users to interact with databases using natural language.

## Features

- Convert natural language queries to SQL queries
- Support for multiple database systems
- Easy to integrate with existing applications

## Installation

To install the project, follow these steps:

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd nl2sql
    ```
3.  Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```
4.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the project, follow these steps:

1.  Configure the database connection in `config.py`.
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  Enter your natural language query when prompted.
4.  The SQL query will be generated and displayed.

## working incrementally