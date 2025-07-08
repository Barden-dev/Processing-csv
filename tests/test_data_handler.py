import pytest
from processing_csv.data_handler import load_data_from_csv

@pytest.mark.parametrize(
    "file_content, expected_result",
    [
        ("id,name\n1,Test", [['id', 'name'], ['1', 'Test']]),
        ("", []),
        (None, None)
    ]
)
def test_load_data(tmp_path, file_content, expected_result):
    
    filepath = tmp_path / "test.csv"
    
    if file_content is not None:
        filepath.write_text(file_content, encoding='utf-8')
    
    actual_result = load_data_from_csv(filepath)
    
    assert actual_result == expected_result