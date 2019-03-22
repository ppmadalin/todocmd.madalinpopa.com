# test_todocmd.py

from src.command import Command
import pytest


@pytest.fixture
def resource():
    com = Command('task')
    return com


def test_init_command(resource):
    tasks = Command('test')
    assert isinstance(tasks, Command)


def test_add_task_command(resource):
    # set the expected result
    expected = "test"

    # create mock object for add_task function
    # add_task_mock = mocker.patch.object(Command, "add_task")

    # set the returned value
    # add_task_mock.return_value = expected

    # initiate the class
    # comm = Command('test')

    # call the function
    # add_task_mock.assert_any_call('test', 'test')
    assert expected == resource.add_task('test')
