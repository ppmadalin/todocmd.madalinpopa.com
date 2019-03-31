# test_interface.py
# standard library
from datetime import date

# third party library
import unittest

# local import
from src.exception import InvalidTaskNumber
from src.command import Command
from src.task import Task
from src.todocmd import load_tasks
from src.todocmd import add_task
from src.todocmd import update_task
from src.todocmd import delete_task
from src.todocmd import list_tasks
from src.todocmd import save_task


class TestCommand(unittest.TestCase):

    def setUp(self):
        """ Initiate a command with a list of tasks """

        # tasks
        task1 = Task('task1', 'task1 note', date.today(), date.today())
        task2 = Task('Task2', 'task2 note', date.today(), date.today())
        task3 = Task('Task3', 'task3 note', date.today(), date.today())

        self.inputs = {'option': 6,
                       'task_number': '5',
                       'task_name': 'Name',
                       'task_note': 'Note',
                       'task_start': '2019-20-03',
                       'task_end': '2019-22-03', }

        # create a command
        self.com = Command([task1, task2, task3])

    def test_load_tasks(self):
        """ Tests if a list of tasks is returned """
        # load tasks
        task_list = load_tasks()

        # test that returns a list
        self.assertIsInstance(task_list, list)

        # test the number of taks
        expected = 3
        self.assertEqual(expected, len(self.com.tasks))

        # test task object
        self.assertIsInstance(task_list[0], Task)

    def test_add_task(self):
        """ Test the if the task is added """
        # user inputs
        self.inputs['option'] = 1

        # add task
        add_task(self.inputs, self.com)

        # get the lenght of tasks
        lenght = len(self.com.tasks)

        # test if the task id added
        self.assertEqual(lenght, 4)

    def test_update_task_invalid_number_exception(self):
        """ Test if the exception is throw """
        # define some inputs
        self.inputs['option'] = 2
        self.inputs['task_number'] = 'invalid_task_number'

        # raise an exception if the task number is invalid
        with self.assertRaises(InvalidTaskNumber):
            update_task(self.inputs, self.com)

        self.inputs['option'] = 6

        # raise an exception if the task number is not in the list
        with self.assertRaises(InvalidTaskNumber):
            update_task(self.inputs, self.com)

    def test_update_task(self):
        """ Test if a task is updated """
        # user inputs
        self.inputs['option'] = 2
        self.inputs['task_number'] = '0'

        # update the task
        update_task(self.inputs, self.com)

        # get the updated task and check the name
        task = self.com.get(0)
        self.assertEqual(task.name, 'Name')

    def test_delete_task_invalid_number_exception(self):
        """ Test if a InvalidTaskNumber exception is raised """
        # define some inputs
        self.inputs['option'] = 6
        self.inputs['task_number'] = 'invalid option'

        # raise an exception if the task number is invalid
        with self.assertRaises(InvalidTaskNumber):
            delete_task(self.inputs, self.com)

        self.inputs['task_number'] = '5'

        # raise an exception if the task number is not in the list
        with self.assertRaises(InvalidTaskNumber):
            delete_task(self.inputs, self.com)

    def test_delete_task(self):
        """ Test if the task is deleted """
        # define inputs
        self.inputs['task_number'] = '0'

        # get the current lenght of the tasks list
        lenght = len(self.com.tasks)

        # delete the task
        delete_task(self.inputs, self.com)

        # check if the tasks lenght is with one less
        self.assertLess(len(self.com.tasks), lenght)

    def test_list_tasks(self):
        """ Test if the tasks are listed """
        # return true if the tasks are displayed
        self.assertTrue(list_tasks)

    def test_save_tasks(self):
        """ Test if the tasks are saved """
        with self.assertRaises(SystemExit) as e:
            save_task(self.inputs, self.com)
            self.assertEqual(e.exception, 0)
