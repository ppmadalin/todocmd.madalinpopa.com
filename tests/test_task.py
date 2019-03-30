# test_task.py
from src.task import Task
import unittest


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task('Task1', 'simple note', '2019-21-3', '2019-22-3')

    def test_init(self):
        """ Test if the taks is instance of Task class """
        self.assertIsInstance(self.task, Task)

    def test_task_unique_id(self):
        """Test if the id is unique for each task"""
        task1 = Task('Task1', 'simple note', '2019-21-3', '2019-22-3', False)
        task2 = Task('Task2', 'note task', '2019-12-4', '2019-14-5', True)
        task_id1 = task1.id
        task_id2 = task2.id
        # should not be equal
        self.assertNotEqual(task_id1, task_id2)

    def test_task_display(self):
        """ Test if the task is displayed only with name """
        expected = "Task1"

        self.assertEqual(expected, str(self.task))

    def test_get_id(self):
        """ Test if the id is returned """
        # create a task and get its id
        expected = self.task.id
        print(f'Task id: {expected}')
        self.assertEqual(expected, self.task.id)
