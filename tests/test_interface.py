# test_interface.py
# standard library
from datetime import date

# third party library
import unittest

# local import
from src.command import Command
from src.task import Task
from src.todocmd import load_tasks
from src.todocmd import add_task
from src.todocmd import update_task
# from src.todocmd import delete_tasks


class TestCommand(unittest.TestCase):

    def setUp(self):
        """ Initiate a command with a list of tasks """

        # tasks
        task1 = Task('task1', 'task1 note', date.today(), date.today())
        task2 = Task('Task2', 'task2 note', date.today(), date.today())
        task3 = Task('Task3', 'task3 note', date.today(), date.today())

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
        inputs = {'option': 1,
                  'task_name': 'Task Name',
                  'task_note': 'Simple Note',
                  'task_start': '2019-23-04',
                  'task_end': '2019-24-04', }
        # add task
        add_task(inputs, self.com)

        # get the lenght of tasks
        lenght = len(self.com.tasks)

        # test if the task id added
        self.assertEqual(lenght, 4)

    def test_update_task(self):
        """ Test if a task is updated """
        # user inputs
        inputs = {'option': 1,
                  'task_number': self.com.tasks[0],
                  'taks_name': 'Name',
                  'task_note': 'Note',
                  'task_start': '2019-20-03',
                  'task_end': '2019-22-03', }

        # update the task
        update_task(inputs, self.com)

        # get the updated task and check the name
        task = self.com.get(0)
        self.assertEqual(task.name, 'Name')
