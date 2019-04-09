# test_controller.py
"""
This modules is used to test all the Terminal
Controller actions.

Actions that will be tested are the following:

    - load_tasks()
    - add_task()
    - update_task()
    - delete_task()
    - list_tasks()

"""

# standard lib imports
import unittest
from datetime import date

# local imports
from src.controller.basectrl import BaseController
from src.controller.termctrl import TerminalController
from src.exception import InvalidTaskNumber
from src.initdata import Data
from src.model.task import Task
from todo import DATA_FILE


class TestTerminalController(unittest.TestCase):

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
        self.com = BaseController([task1, task2, task3])

    def test_load_tasks(self):
        """ Tests if a list of tasks is returned """
        # load tasks
        task_list = Data.load_from_csv_file(DATA_FILE)

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
        TerminalController.add_task(self.inputs, self.com)

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
            TerminalController.update_task(self.inputs, self.com)

        self.inputs['option'] = 6

        # raise an exception if the task number is not in the list
        with self.assertRaises(InvalidTaskNumber):
            TerminalController.update_task(self.inputs, self.com)

    def test_update_task(self):
        """ Test if a task is updated """
        # user inputs
        self.inputs['option'] = 2
        self.inputs['task_number'] = '0'

        # update the task
        TerminalController.update_task(self.inputs, self.com)

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
            TerminalController.delete_task(self.inputs, self.com)

        self.inputs['task_number'] = '5'

        # raise an exception if the task number is not in the list
        with self.assertRaises(InvalidTaskNumber):
            TerminalController.delete_task(self.inputs, self.com)

    def test_delete_task(self):
        """ Test if the task is deleted """
        # define inputs
        self.inputs['task_number'] = '0'

        # get the current lenght of the tasks list
        lenght = len(self.com.tasks)

        # delete the task
        TerminalController.delete_task(self.inputs, self.com)

        # check if the tasks lenght is with one less
        self.assertLess(len(self.com.tasks), lenght)

    def test_list_tasks(self):
        """ Test if the tasks are listed """
        # return true if the tasks are displayed
        self.assertTrue(TerminalController.list_tasks)

    def test_save_tasks(self):
        """ Test if the tasks are saved """
        save = Data.save_to_csv_file(self.inputs, self.com, DATA_FILE)
        self.assertTrue(save)


if __name__ == '__main__':
    unittest.main()
