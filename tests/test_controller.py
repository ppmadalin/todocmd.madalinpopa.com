# test_controller.py
""" This modules is used to test all the supported commands """

# standard lib imports
import unittest
from datetime import date
# local imports
from todo import DATA_FILE
from src.model.task import Task
from src.view.termview import TerminalView
from src.cmdargs import CommandArgs
from src.controller.basectrl import BaseController
from src.controller.initdata import Data
from src.controller.termctrl import add_task
from src.controller.termctrl import delete_task
from src.controller.termctrl import update_task


class TestController(unittest.TestCase):

    def setUp(self):
        """ Tests setup """
        # options
        self.options = dict()

        # tasks
        task1 = Task('task1', 'task1 note', date.today(), date.today())
        task2 = Task('Task2', 'task2 note', date.today(), date.today())
        task3 = Task('Task3', 'task3 note', date.today(), date.today())

        # command
        self.com = BaseController([task1, task2, task3])

        # initiate the argparse
        self.parse = CommandArgs()

    def test_cmd_start(self):
        """ Test if the command line start is passed """
        # passed args
        args = self.parse.parse_args(['-i'])

        # test given args
        self.assertTrue(args.interactive)

    def test_cmd_list_tasks(self):
        """ Test display all the tasks """
        # passed args
        args = self.parse.parse_args(['-l'])

        # test given args
        self.assertTrue(args.tasks)

        # get a list of tasks and check if is not empty
        if args.tasks:
            list_of_tasks = Data.load_from_csv_file(DATA_FILE)

        self.assertTrue(len(list_of_tasks) > 0)

        # test first task in the list
        tasks = Data.load_from_csv_file(DATA_FILE)
        self.assertIsInstance(tasks[0], Task)

    def test_cmd_list_one_task(self):
        """ Test if only one task is listed """
        # pass args
        args = self.parse.parse_args(['-l', '-t', 0])

        # test given args
        self.assertTrue(args.tasks and args.task[0] == 0)

        # list task
        task = self.com.tasks[args.task[0]]
        self.assertTrue(TerminalView.display_tasks([task]))

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
        args = self.parse.parse_args(['-d', '-t', 0])

        # test given command
        self.assertTrue(args.delete)
        self.assertTrue(args.delete and args.task[0] == 0)

        # test deleting a task
        self.options['option'] = '--delete'
        self.options['task_number'] = args.task[0]

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

    def test_cmd_select_task(self):
        """ Test if a task is selectd """
        # passed args
        args = self.parse.parse_args(['-t', 0, ])

        # test given arguments
        self.assertTrue(args.task[0] == 0)

    def test_cmd_name_task(self):
        """ Test if task name is updated"""
        # passed args
        args = self.parse.parse_args(['-t', 0, '--name', 'name'])

        # test given arguments
        self.assertTrue(args.task[0] == 0)
        self.assertTrue(args.task_name[0] == 'name')

        # get task 0
        task0 = self.com.tasks[0]
        previous_name = task0.name

        # update task
        self.options['option'] = 'update'
        self.options['task_number'] = args.task[0]
        self.options['task_name'] = args.task_name[0]
        self.options['task_note'] = task0.note
        self.options['task_start'] = task0.start_date
        self.options['task_end'] = task0.end_date
        update_task(self.options, self.com)

        # test if the name has changed
        self.assertNotEqual(previous_name, self.com.tasks[0].name)


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
        save = Data.save_to_csv_file(self.inputs, self.com, DATA_FILE)
        self.assertTrue(save)

if __name__ == '__main__':
    unittest.main()
