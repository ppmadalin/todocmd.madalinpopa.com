# test_interface.py
# standard library
from datetime import date

# third party library
import pytest

# local import
from src.task import Task
from src.command import Command
from src.todocmd import load_tasks
# from src.todocmd import add_task
# from src.todocmd import update_task
# from src.todocmd import delete_tasks


@pytest.fixture
def command():
    """ Initiate a command with a list of tasks """
    # tasks
    task1 = Task('task1', 'task1 note', date.today(), date.today())
    task2 = Task('Task2', 'task2 note', date.today(), date.today())
    task3 = Task('Task3', 'task3 note', date.today(), date.today())

    # create a command
    com = Command([task1, task2, task3])

    # return command
    return com


def test_load_tasks(command):
    """ Tests if a list of tasks is returned """
    # load tasks
    task_list = load_tasks()

    # test that returns a list
    assert isinstance(task_list, list)

    # test the number of taks
    expected = 3
    assert expected == len(task_list)

    # test task object
    assert isinstance(task_list[0], Task)
