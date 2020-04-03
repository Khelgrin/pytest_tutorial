
from Filereader import read_from_file
from unittest.mock import MagicMock
import pytest

# def test_can_call_read_from_file():
#     read_from_file("myfile")
@pytest.fixture()
def mock_open(monkeypatch):
    mockfile = MagicMock()
    mockfile.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mockfile)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


def test_returns_correct_string(monkeypatch, mock_open):
    mock_exist = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exist)
    result = read_from_file("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"


def test_throws_exception_with_no_file(monkeypatch, mock_open):
    mock_exist = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exist)
    with pytest.raises(Exception):
        result = read_from_file("blah")