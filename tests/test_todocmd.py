# test_todocmd.py
import unittest
from datetime import date
from src.controller.basectrl import BaseController
from src.model.task import Task


class TestTodocmd(unittest.TestCase):
    def setUp(self):
        """ Initiate two tasks and a command """
        task1 = Task('task1', 'task1 note', date.today(), date.today())
        task2 = Task('Task2', 'task2 note', date.today(), date.today())

        self.com = BaseController([task1, task2])

    def test_init_command(self):
        """ test if the resource is instance of BaseController """
        self.assertIsInstance(self.com, BaseController)

    def test_add_task_command(self):
        """ returns Task if the task is added """
        # create a task
        task = Task('task name', 'task note', date.today(), date.today())

        # set the expected result
        expected = task

        # should return task
        self.assertEqual(expected, self.com.add(task))

    def test_get_all_tasks_command(self):
        """ test if returns a list of tasks """
        # get all taks
        tasks = self.com.tasks

        # check how many tasks are in list
        assert len(tasks) == 2
        self.assertEqual(len(tasks), 2)

        # check if each task is instance of Task
        for task in tasks:
            self.assertIsInstance(task, Task)

    def test_get_task_command(self):
        """ returns a task from list """
        # create a task
        task1 = self.com.get(1)
        task2 = self.com.get(0)

        # get the task
        self.assertIsInstance(task1, Task)
        self.assertIsInstance(task2, Task)

    def test_get_invalid_task_number_command(self):
        """ tests if a invalid task number is provided """
        # get the number of tasks
        lenght = len(self.com.tasks)

        # catch exception
        with self.assertRaises(IndexError):
            self.com.get(lenght + 1)

    def test_update_task_command(self):
        """ return task that was edited """
        # get a task
        task = self.com.tasks[0]

        # change the task
        task.name = 'Changed Task'
        # update task
        changed_task = self.com.update(task)
        # check task name
        assert changed_task.name == 'Changed Task'
        self.assertEqual(changed_task.name, 'Changed Task')

    def test_delete_task_command(self):
        """ Test if task deletion works """
        # get a task
        task = self.com.tasks[0]

        # delete task
        deleted_task = self.com.delete(task)

        # check lenght of list with all tasks
        self.assertLess(len(self.com.tasks), 2)

        # check if returned taks is the same as given task
        self.assertEqual(deleted_task.id, task.id)
