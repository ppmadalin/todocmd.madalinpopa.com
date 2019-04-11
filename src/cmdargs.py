# cmdargs.py
"""
This modules holds all the supported command
line operations
"""

from argparse import ArgumentParser
from src.initdata import Data


class CommandArgs(ArgumentParser):

    options: dict

    def __init__(self, DATA_FILE):
        super().__init__()
        self.DATA_FILE = DATA_FILE
        self.options = dict()
        self.prog = 'TO-DO'
        self.description = 'Simple TO-DO app'

        self.add_argument('-i', '--interactive',
                          dest='interactive',
                          action='store_true',
                          help='Start command line interface',
                          default=False, )

        self.add_argument('-l', '--list',
                          dest='tasks',
                          help='List all the tasks',
                          action='store_true', )

        self.add_argument('-a', '--add',
                          dest='add',
                          nargs=4,
                          help='Add a new task',
                          action='store', )

        self.add_argument('-d', '--delete',
                          dest='delete',
                          help='Delete task',
                          action='store_true', )

        self.add_argument('-u', '--update',
                          dest='update',
                          help='Update task',
                          action='store',
                          nargs=4, )

        self.add_argument('-t', '--task',
                          dest='task',
                          help='Pick a task number',
                          action='store',
                          nargs=1,
                          type=int, )

        self.add_argument('-m', '--mark',
                          dest='mark',
                          help='Mark a task done or undone',
                          action='store',
                          nargs=1,
                          type=str, )

        self.add_argument('--name',
                          dest='task_name',
                          help='Task name',
                          action='store',
                          nargs=1,
                          type=str, )

        self.add_argument('--note',
                          dest='task_note',
                          help='Task note',
                          action='store',
                          nargs=1,
                          type=str, )

        self.add_argument('--start',
                          dest='task_start',
                          help='Task start date',
                          action='store',
                          nargs=1, )

        self.add_argument('--due',
                          dest='task_due',
                          help='Task due date',
                          action='store',
                          nargs=1, )

    def list_tasks(self, controller, command, logger):
        """
        List all the tasks
        """
        args = self.parse_args()
        if args.tasks:
            self.options['option'] = '-l --list'
            controller.list_tasks(self.options, command, logger)

    def add_task(self, controller, command, logger):
        """
        Add a new task in list
        """
        args = self.parse_args()
        if args.add:
            self.options['option'] = '--add'
            self.options['task_name'] = args.add[0]
            self.options['task_note'] = args.add[1]
            self.options['task_start'] = args.add[2]
            self.options['task_end'] = args.add[3]
            controller.add_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)

    def delete_task(self, controller, command, logger):
        """
        Delete a specific task
        """
        args = self.parse_args()
        if args.delete and args.task:
            self.options['option'] = '--delete'
            self.options['task_number'] = args.task[0]
            controller.delete_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)
        elif args.delete and not args.task:
            print('You must specify a task number')
            print('Usage: -t <task_number> -d')

    def update_task(self, controller, command, logger):
        """
        Update a specific task
        """
        args = self.parse_args()
        if args.task and args.update:
            self.options['option'] = '-u'
            self.options['task_number'] = args.task[0]
            self.options['task_name'] = args.update[0]
            self.options['task_note'] = args.update[1]
            self.options['task_start'] = args.update[2]
            self.options['task_end'] = args.update[3]
            controller.update_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)
        elif args.update and not args.task:
            print('You must specify a task number')
            print('Usage: -t <task_number> -u <name> <note> <start> <due>')

    def update_task_name(self, controller, command, logger):
        """
        Update task's name
        """
        args = self.parse_args()
        if args.task and args.task_name:
            self.options['option'] = '--name'
            self.options['task_number'] = args.task[0]
            self.options['task_name'] = args.task_name[0]
            controller.update_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)
        elif args.task_name and not args.task:
            print('You must specify a task number')
            print('Usage: -t <task_number> --name <task_name>')

    def update_task_note(self, controller, command, logger):
        """
        Update task's note
        """
        args = self.parse_args()
        if args.task and args.task_note:
            self.options['option'] = '--note'
            self.options['task_number'] = args.task[0]
            self.options['task_start'] = args.task_note[0]
            controller.update_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)
        elif args.task_note and not args.task:
            print('You must specify a task number')
            print('Usage: -t <task_number> --note <task_note>')

    def update_task_start(self, controller, command, logger):
        """
        Update task's start date
        """
        args = self.parse_args()
        if args.task and args.task_start:
            self.options['option'] = '--start'
            self.options['task_number'] = args.task[0]
            self.options['task_start'] = args.task_start[0]
            controller.update_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)
        elif args.task_start and not args.task:
            print('You must specify a task number')
            print('Usage: -t <task_number> --start <task_start_date>')

    def update_task_due(self, controller, command, logger):
        """
        Update task's due date
        """
        args = self.parse_args()
        if args.task and args.task_due:
            self.options['option'] = '--due'
            self.options['task_number'] = args.task[0]
            self.options['task_end'] = args.task_due[0]
            controller.update_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)
        elif args.task_start and not args.task:
            print('You must specify a task number')
            print('Usage: -t <task_number> --start <task_start_date>')

    def mark_task(self, controller, command, logger):
        """
        Mark task
        """
        args = self.parse_args()
        if args.task and args.mark:
            self.options['option'] = '--mark'
            self.options['task_number'] = args.task[0]
            self.options['task_status'] = args.mark[0]
            controller.mark_task(self.options, command, logger)
            Data.save_to_csv_file(self.options,
                                  command, self.DATA_FILE, logger)
        elif args.mark and not args.task:
            print('You must specify a task number')
            print('Usage: -t <task_number> --mark done/undone')


class CommandOptions:
    pass
