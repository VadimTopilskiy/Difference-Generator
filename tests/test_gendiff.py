import json
import pytest

from gendiff import generate_diff
from tests import FIXTURES_PATH
from tests import FIXTURES_DIR


#
#
# @pytest.fixture
# def open_files():
#     file1 = json.load(open('tests/fixtures/file1.json'))
#     file2 = json.load(open('tests/fixtures/file2.json'))
#     return file1, file2
def expected_str():
    with open(f'{FIXTURES_DIR}expected_result.txt') as f:
        expected_str = f.read()
    return expected_str


def test_if_key_in_both_files():
    with open(f'{FIXTURES_PATH}expected_result.txt') as f:
        expected_str = f.read()
    print(generate_diff(f'{FIXTURES_PATH}file1.yml', f'{FIXTURES_PATH}file2.yml'))
    assert generate_diff(f'{FIXTURES_PATH}file1.yml', f'{FIXTURES_PATH}file2.yml') == expected_str
def _get_file_path(file_name: str) -> str:
    return f'{FIXTURES_DIR}{file_name}'


JSON1 = _get_file_path('file1.json')
JSON2 = _get_file_path('file2.json')
YAML1 = _get_file_path('file1.yml')
YAML2 = _get_file_path('file2.yml')


@pytest.mark.parametrize(
    "filepath1, filepath2",
    [
        (JSON1, JSON2),
        (YAML1, YAML2)
    ],
    ids=[
        "file1.json - file2.json",
        "file1.yml - file2.yml",
    ],
)
def test_generate_diff(filepath1, filepath2):
    assert generate_diff(filepath1, filepath2) == expected_str()
