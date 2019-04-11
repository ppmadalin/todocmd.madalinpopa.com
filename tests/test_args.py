# test_args.py
"""
This module tests all the command line args that are
passed ot todo.py file.

The following arguments will be tested:


-i --interactive
-t --task <task_number>
-l --list
-l -t <task_number>
-u --update <task_name> <task_note> <task_start> <task_due>  -t <task_number>
-d --delete -t <task_number>
-a --add <task_name> <task_note> <task_start> <task_due>
-m --mark <status> -t <task_number>
--name <task_name> -t <task_number>
--note <task_note> -t <task_number>
--start <task_start> -t <task_number>
--due <task_due> -t <task_number>

"""
# standard lib imports
import unittest
from datetime import date

# local imports
from todo import DATA_FILE
from src.model.task import Task
from src.view.termview import TerminalView
from src.cmdargs import CommandArgs
from src.controller.basectrl import BaseController
from src.initdata import Data
from src.controller.termctrl import TerminalController


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
        TerminalController.add_task(self.options, self.com)

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
        TerminalController.delete_task(self.options, self.com)
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
        TerminalController.update_task(self.options, self.com)
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
        TerminalController.update_task(self.options, self.com)

        # test if the name has changed
        self.assertNotEqual(previous_name, self.com.tasks[0].name)

    def test_cmd_note_task(self):
        """ Test if task name is updated"""
        # passed args
        args = self.parse.parse_args(['-t', 0, '--note', 'note'])

        # test given arguments
        self.assertTrue(args.task[0] == 0)
        self.assertTrue(args.task_note[0] == 'note')

        # get task 0
        task0 = self.com.tasks[0]
        previous_note = task0.note

        # update task
        self.options['option'] = 'update'
        self.options['task_number'] = args.task[0]
        self.options['task_name'] = task0.name
        self.options['task_note'] = args.task_note[0]
        self.options['task_start'] = task0.start_date
        self.options['task_end'] = task0.end_date
        TerminalController.update_task(self.options, self.com)

        # test if the name has changed
        self.assertNotEqual(previous_note, self.com.tasks[0].note)

    def test_update_task_start(self):
        """ Test if task start date is updated"""
        # passed args
        args = self.parse.parse_args(['-t', 0, '--start', 'start'])

        # test given arguments
        self.assertTrue(args.task[0] == 0)
        self.assertTrue(args.task_start[0] == 'start')

        # get task 0
        task0 = self.com.tasks[0]
        previous_start_date = task0.start_date

        # update task
        self.options['option'] = 'update'
        self.options['task_number'] = args.task[0]
        self.options['task_name'] = task0.name
        self.options['task_note'] = task0.note
        self.options['task_start'] = args.task_start[0]
        self.options['task_end'] = task0.end_date
        TerminalController.update_task(self.options, self.com)

        # test if the name has changed
        self.assertNotEqual(previous_start_date, self.com.tasks[0].start_date)

    def test_update_task_due(self):
        """ Test if task due date is updated"""
        # passed args
        args = self.parse.parse_args(['-t', 0, '--due', 'due'])

        # test given arguments
        self.assertTrue(args.task[0] == 0)
        self.assertTrue(args.task_due[0] == 'due')

        # get task 0
        task0 = self.com.tasks[0]
        previous_due_date = task0.end_date

        # update task
        self.options['option'] = 'update'
        self.options['task_number'] = args.task[0]
        self.options['task_name'] = task0.name
        self.options['task_note'] = task0.note
        self.options['task_start'] = task0.start_date
        self.options['task_end'] = args.task_due[0]
        TerminalController.update_task(self.options, self.com)

        # test if the name has changed
        self.assertNotEqual(previous_due_date, self.com.tasks[0].end_date)

    def test_update_task_status(self):
        """ Test if a task is mark as done """
        # passed args
        args = self.parse.parse_args(['-t', 0, '-m', 'done'])

        # test given arguments
        self.assertTrue(args.task[0] == 0)
        self.assertTrue(args.mark[0] == 'done')

        # get task 0
        task0 = self.com.tasks[0]

        # update status
        self.options['option'] = 'mark'
        self.options['task_number'] = args.task[0]
        self.options['task_status'] = args.mark[0]
        TerminalController.mark_task(self.options, self.com)

        # test if the status has been changed
        self.assertTrue(task0.status)
