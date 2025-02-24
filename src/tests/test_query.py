import pytest

from src.utils.common_utils import clean_generation_result


@pytest.mark.parametrize(
    "input_text,expected_output",
    [
        (
            '```json\n{"sql": "SELECT * FROM airports;"}\n```',
            ' {"sql": "SELECT * FROM airports"} ',
        ),
        ('{"sql": "SELECT * FROM airlines;"}', '{"sql": "SELECT * FROM airlines"}'),
        (
            '```\n{"sql": "SELECT * FROM flights LIMIT 1;"}\n```',
            ' {"sql": "SELECT * FROM flights LIMIT 1"} ',
        ),
    ],
)
def test_clean_generation_result(input_text, expected_output):
    result = clean_generation_result(input_text)
    assert result == expected_output
