from tests import FIXTURES_DIR


def expected_str():
    with open(f'{FIXTURES_DIR}flat_output.txt') as f:
def _get_expected_output_by(file_name: str) -> str:
    print(f'file name=', file_name)
    with open(f'{FIXTURES_DIR}{file_name}') as f:
        expected_str = f.read()
    return expected_str


def _get_file_path(file_name: str) -> str:
def _get_file_path_by(file_name: str) -> str:
    return f'{FIXTURES_DIR}{file_name}'


JSON1 = _get_file_path('file1.json')
JSON2 = _get_file_path('file2.json')
YAML1 = _get_file_path('file1.yml')
YAML2 = _get_file_path('file2.yml')
JSON1 = _get_file_path_by('file1.json')
JSON2 = _get_file_path_by('file2.json')
YAML1 = _get_file_path_by('file1.yml')
YAML2 = _get_file_path_by('file2.yml')
NESTED_JSON1 = _get_file_path_by('nested_file1.json')
NESTED_JSON2 = _get_file_path_by('nested_file1.json')
NESTED_YAML1 = _get_file_path_by('nested_file1.yml')
NESTED_YAML2 = _get_file_path_by('nested_file1.yml')
FLAT_OUTPUT = _get_expected_output_by('flat_output.txt')
NESTED_OUTPUT = _get_expected_output_by('nested_output.txt')


@pytest.mark.parametrize(
    'filepath1, filepath2',
    'filepath1, filepath2, output',
    [
        (JSON1, JSON2),
        (YAML1, YAML2)
        (JSON1, JSON2, FLAT_OUTPUT),
        (YAML1, YAML2, FLAT_OUTPUT),
        (NESTED_JSON1, NESTED_JSON2, NESTED_OUTPUT),
        (NESTED_YAML1, NESTED_YAML2, NESTED_OUTPUT),
    ],
    ids=[
        'file1.json - file2.json',
        'file1.yml - file2.yml',
        'flat_file1.json - flat_file2.json',
        'flat_file1.yml - flat_file2.yml',
        'nested_file1.json - nested_file2.json',
        'nested_file1.yml - nested_file2.yml'
    ],
)
def test_generate_diff(filepath1, filepath2):
    assert generate_diff(filepath1, filepath2) == expected_str()
def test_generate_diff(filepath1, filepath2, output):
    assert generate_diff(filepath1, filepath2) == output
