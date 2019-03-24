# test_todocmd.py

import pytest
from datetime import date
from src.command import Command
from src.task import Task


@pytest.fixture
def resource():
    """ Initiate a command with a list of two tasks """
    task1 = Task('task1', 'task1 note', date.today(), date.today())
    task2 = Task('Task2', 'task2 note', date.today(), date.today())
    com = Command([task1, task2])
    return com


def test_init_command(resource):
    """ test if the resource is instance of Command """
    assert isinstance(resource, Command)


def test_add_task_command(resource):
    """ returns Task if the task is added """
    # create a task
    task = Task('task name', 'task note', date.today(), date.today())

    # set the expected result
    expected = task

    # should return task
    assert expected == resource.add(task)


def test_get_all_tasks_command(resource):
    """ test if returns a list of tasks """
    # get all taks
    tasks = resource.tasks

    # check how many tasks are in list
    assert len(tasks) == 2

    # check if each task is instance of Task
    for task in tasks:
        assert isinstance(task, Task)


def test_get_task_command(resource):
    """ returns a task from list """
    # create a task
    task = resource.get(1)

    # get the task
    assert isinstance(task, Task)


def test_update_task_command(resource):
    """ return task that was edited """
    # get a task
    task = resource.tasks[0]

    # change the task
    task.name = 'Changed Task'

    # update task
    changed_task = resource.update(task)

    # check task name
    assert changed_task.name == 'Changed Task'


def test_delete_task_command(resource):
    """ Test if task deletion works """
    # get a task
    task = resource.tasks[0]

    # delete task
    deleted_task = resource.delete(task)

    # check lenght of list with all tasks
    assert len(resource.tasks) < 2

    # check if returned taks is the same as given task
    assert deleted_task.id == task.id
