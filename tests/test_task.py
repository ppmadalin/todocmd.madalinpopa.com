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
    """Test if the instance of task is instance of Task"""
    # test if is instance of Task:
    assert isinstance(resource, Task)


def test_task_unique_id(resource):
    """Test if the id is unique for each task"""
    task1 = Task('Task1', 'simple note', '2019-21-3', '2019-22-3', False)
    task2 = Task('Task2', 'note task', '2019-12-4', '2019-14-5', True)
    task_id1 = task1.id
    task_id2 = task2.id
    # should not be equal
    assert task_id1 != task_id2


def test_task_display(resource):
    """ Test if the task is displayed only with name """
    expected = "Task1"
    assert expected == str(resource)


def test_get_id(resource):
    """ Test if the id is returned """
    # create a task and get its id
    expected = resource.id
    print(f'Task id: {expected}')
    assert expected == resource.id
