# test_task.py
from src.task import Task
import pytest


@pytest.fixture
def resource():
    name = 'Task1'
    note = 'simple task note'
    start_date = '2019-21-3'
    end_date = '2019-22-3'
    status = True
    task = Task(name, note, start_date, end_date, status)
    return task


def test_init(resource):
    # test if is instance of Task:
    assert isinstance(resource, Task)
