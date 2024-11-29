import pytest
import os
import json
from src.entity.Task import Task
from src.repositories.TaskRepository import MockTaskRepository


@pytest.fixture
def temp_json_file():
    file_path = "test_tasks.json"
    initial_data = [
        {
            "id": 1,
            "title": "Task 1",
            "description": "Description 1",
            "category": "Work",
            "date_exp": "2024-11-30",
            "priority": "High"
        },
        {
            "id": 2,
            "title": "Task 2",
            "description": "Description 2",
            "category": "Personal",
            "date_exp": "2024-12-01",
            "priority": "Low"
        }
    ]
    with open(file_path, "w") as f:
        json.dump(initial_data, f, indent=4)
    yield file_path
    os.remove(file_path)


@pytest.fixture
def repository(temp_json_file):
    return MockTaskRepository(temp_json_file)


def test_load_tasks(repository):
    tasks = repository.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].category == "Personal"


def test_create_task(repository):
    new_task = Task(3, "Task 3", "Description 3", "Work", "2024-12-05", "Medium")
    repository.create_task(new_task)
    tasks = repository.get_all_tasks()
    assert len(tasks) == 3
    assert tasks[-1].title == "Task 3"


def test_create_duplicate_task(repository):
    duplicate_task = Task(1, "Duplicate Task", "Duplicate Description", "Work", "2024-12-05", "Medium")
    with pytest.raises(ValueError):
        repository.create_task(duplicate_task)


def test_delete_task_by_id(repository):
    success = repository.delete_task_by_id(1)
    tasks = repository.get_all_tasks()
    assert success is True
    assert len(tasks) == 1
    assert tasks[0].id != 1


def test_delete_nonexistent_task(repository):
    success = repository.delete_task_by_id(99)
    assert success is False


def test_get_all_tasks_by_category(repository):
    tasks = repository.get_all_tasks_by_category("Work")
    assert len(tasks) == 1
    assert tasks[0].title == "Task 1"


def test_update_task_title(repository):
    success = repository.update_task_title(1, "Updated Task 1")
    tasks = repository.get_all_tasks()
    assert success is True
    assert tasks[0].title == "Updated Task 1"


def test_find_task_by_id(repository):
    task = repository.find_task_by_id(1)
    assert task.title == "Task 1"


def test_find_tasks_by_keyword(repository):
    task = repository.find_task_by_keyword("Description 1")
    assert task.id == 1


def test_update_task_status(repository):
    success = repository.update_task_status(1, "Completed")
    tasks = repository.get_all_tasks()
    assert success is True
    assert tasks[0].status == "Completed"
