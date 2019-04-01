# test_commands.py
""" This modules is used to test all the supported commands """

# standard lib imports
import unittest
import argparse
from datetime import date
# local imports
from main import DATA_FILE
from src.task import Task
from src.command import CommandLine
from src.command import Command
from src.todocmd import load_tasks
from src.todocmd import add_task
from src.todocmd import delete_task
from src.todocmd import update_task


class TestCommandArgs(unittest.TestCase):

    def setUp(self):
        """ Tests setup """
        # options
        self.options = dict()

        # tasks
        task1 = Task('task1', 'task1 note', date.today(), date.today())
        task2 = Task('Task2', 'task2 note', date.today(), date.today())
        task3 = Task('Task3', 'task3 note', date.today(), date.today())

        # command
        self.com = Command([task1, task2, task3])

        # initiate the argparse
        self.parse = CommandLine()

    def test_cmd_start(self):
        """ Test if the command line start is passed """
        # passed args
        args = self.parse.parse_args(['start', 1])

        # test given args
        self.assertTrue(args.start)

    def test_cmd_list_tasks(self):
        """ Test display all the tasks """
        # passed args
        args = self.parse.parse_args(['-l'])

        # test given args
        self.assertTrue(args.tasks)

        # get a list of tasks and check if is not empty
        if args.tasks:
            list_of_tasks = load_tasks(DATA_FILE)

        self.assertTrue(len(list_of_tasks) > 0)

        # test first task in the list
        tasks = load_tasks(DATA_FILE)
        self.assertIsInstance(tasks[0], Task)

    def test_cmd_add_new_task(self):
        """ Test add new task using comand args """
        # passed args
        args = self.parse.parse_args(['-a',
                                      'Task1',
                                      'simple note',
                                      '2019-04-20',
                                      '2019-04-22', ])

        # test given args
        self.assertTrue(len(args.add) == 4)

        # test first argument
        self.assertEqual(args.add[0], 'Task1')

        # test adding new task
        self.options['option'] = '--add'
        self.options['task_name'] = args.add[0]
        self.options['task_note'] = args.add[1]
        self.options['task_start'] = args.add[2]
        self.options['task_end'] = args.add[3]
        add_task(self.options, self.com)

    def test_cmd_delete_task(self):
        """ Test delete task from command """
        # passed args
        args = self.parse.parse_args(['-d', 0, ])

        # test given command
        self.assertTrue(args.delete[0] == 0)

        # test deleting a task
        self.options['option'] = '--delete'
        self.options['task_number'] = args.delete[0]

        # get the first task
        task = self.com.tasks[0]
        delete_task(self.options, self.com)
        self.assertFalse(task.name == self.com.tasks[0].name)

    def test_cmd_update_task(self):
        """ Test if a task is updated """
        # passed args
        args = self.parse.parse_args(['-t', 0,
                                      '-u', 'name',
                                      'note', 'start_date',
                                      'end_date'])

        # test given arguments
        task_args_len = len(args.task)
        update_args_len = len(args.update)
        self.assertTrue(task_args_len == 1)
        self.assertTrue(update_args_len == 4)

        # test delete a task
        self.options['option'] = '-u'
        self.options['task_number'] = args.task[0]
        self.options['task_name'] = args.update[0]
        self.options['task_note'] = args.update[1]
        self.options['task_start'] = args.update[2]
        self.options['task_end'] = args.update[3]
        update_task(self.options, self.com)
        self.assertTrue(self.com.tasks[0].name == 'name')


if __name__ == '__main__':
    unittest.main()
