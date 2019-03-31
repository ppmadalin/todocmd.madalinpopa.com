# test_commands.py
""" This modules is used to test all the supported commands """

# standard lib imports
import unittest
import argparse

# local imports
from main import DATA_FILE
from src.task import Task
from src.command import Command
from src.todocmd import load_tasks
from src.todocmd import add_task


class TestCommandArgs(unittest.TestCase):

    def setUp(self):
        """ Tests setup """
        # options
        self.options = dict()

        # command
        self.com = Command(load_tasks(DATA_FILE))

        # initiate the argparse
        self.parse = argparse.ArgumentParser(prog='TO-DO',
                                             description='Simple todo app')

        # add optional arguments
        self.parse.add_argument('-l', '--list',
                                dest='tasks',
                                help='List all the tasks',
                                action='store_true',
                                required=False)

        self.parse.add_argument('-a', '--add',
                                dest='add',
                                help='Add a new task',
                                action='store',
                                nargs=4,
                                required=False)

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


if __name__ == '__main__':
    unittest.main()
