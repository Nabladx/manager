from unittest.mock import patch, MagicMock
from my_functions import TaskManager

import pytest

mock_data = [
    {"id": 1, "title": "Fix broomstick", "description": "Fix the broomstick before the match",
     "category": "Maintenance", "due_date": "2024-12-09", "priority": "High", "status": "Not done"},
    {"id": 2, "title": "Learn Patronus", "description": "Learn how to cast Patronus charm", "category": "Learning",
     "due_date": "2024-12-15", "priority": "Medium", "status": "Not done"},
]

@pytest.fixture
def mock_json_data():
    with patch("builtins.open", MagicMock()):
        return mock_data

def mock_input():
    return "1"

@patch("builtins.input", mock_input)
@patch("builtins.print")
def test_main_menu(mock_print):
    task_manager = TaskManager()
    task_manager.main_menu()
    mock_print.assert_called()

@patch("builtins.input", mock_input)
@patch("builtins.print")
def test_task_list(mock_print, mock_json_data):
    task_manager = TaskManager()
    task_manager.task_list()
    assert mock_print.called

@patch("builtins.input", side_effect=["New", "Fix the task", "Work", "2024-12-20", "Высокий", "Не выполнена"])
@patch("builtins.print")
@patch("builtins.open", MagicMock())
def test_add_task(mock_json_data):
    task_manager = TaskManager()
    task_manager.add_task()
    assert len(mock_json_data) == 3

@patch("builtins.input", side_effect=["1", "1", "New Title"])
@patch("builtins.print")
@patch("builtins.open", MagicMock())
def test_change_task(mock_json_data):
    task_manager = TaskManager()
    task_manager.change_task()
    assert mock_json_data[0]["title"] == "New Title"
@patch("builtins.input", side_effect=["1", "1"])
@patch("builtins.print")
@patch("builtins.open", MagicMock())
def test_delete_task(mock_json_data):
    task_manager = TaskManager()
    task_manager.delete_task()
    assert len(mock_json_data) == 1

@patch("builtins.input", side_effect=["1", "Fix broomstick"])
@patch("builtins.print")
def test_search_task_by_keywords(mock_print, mock_json_data):
    task_manager = TaskManager()
    task_manager.search_task()
    assert "Fix broomstick" in str(mock_print.call_args_list)

@patch("builtins.input", side_effect=["2", "Maintenance"])
@patch("builtins.print")
def test_search_task_by_category(mock_print, mock_json_data):
    task_manager = TaskManager()
    task_manager.search_task()
    assert "Fix broomstick" in str(mock_print.call_args_list)

@patch("builtins.input", side_effect=["3", "2"])
@patch("builtins.print")
def test_search_task_by_status(mock_print, mock_json_data):
    task_manager = TaskManager()
    task_manager.search_task()
    assert "Not done" in str(mock_print.call_args_list)
