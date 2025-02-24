import re

def clean_generation_result(result: str) -> str:
    """Cleans the generated SQL query by removing unnecessary characters and whitespace."""

    def _normalize_whitespace(s: str) -> str:
        return re.sub(r"\s+", " ", s).strip()

    return (
        _normalize_whitespace(result)
        .replace("\\n", " ")
        .replace("```sql", "")
        .replace("```json", "")
        .replace('"""', "")
        .replace("```", "")
        .replace(";", "")
    )
