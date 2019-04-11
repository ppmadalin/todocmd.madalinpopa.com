# termctrl.py
"""
This module file contains the commands
for terminal interface.

"""

# local lib imports
from src.view.termview import TerminalView
from src.exception import InvalidTaskNumber
from src.model.task import Task


class TerminalController:

    @staticmethod
    def add_task(options, command, logger=None):
        """ Adds a new task in list """
        if logger:
            logger.info(f'user command is {options["option"]}')
        task_name = options['task_name']
        task_note = options['task_note']
        start_date = options['task_start']
        due_date = options['task_end']
        task = Task(task_name, task_note, start_date, due_date)
        command.add(task)
        print(f'you have added task: {task}')
        if logger:
            logger.info(f'the following task was added {task}')

    @staticmethod
    def update_task(options, command, logger=None):
        """ Updates an existing task """
        if logger:
            logger.info(f'user command is {options["option"]}')
        task_number = str(options['task_number'])
        if not task_number.isdigit():
            raise(InvalidTaskNumber('Please pick a number..'))
        if int(task_number) >= len(command.tasks):
            message = f'Pick a task between 0 and {len(command.tasks)}'
            raise(InvalidTaskNumber(message))
        task = command.get(int(task_number))
        if options.get('task_name') is not None:
            task.name = options['task_name']
        if options.get('task_note') is not None:
            task.note = options['task_note']
        if options.get('task_start') is not None:
            task.start_date = options['task_start']
        if options.get('task_end') is not None:
            task.end_date = options['task_end']
        command.update(task)
        if logger:
            logger.info(f'the following task was updated {task}')
        print(f'You have updated task: {task}')

    @staticmethod
    def delete_task(options, command, logger=None):
        """ Delete a task """
        if logger:
            logger.info(f'user command is {options["option"]}')
        task_number = str(options['task_number'])
        if not task_number.isdigit():
            raise(InvalidTaskNumber('Please pick a number..'))
        if int(task_number) >= len(command.tasks):
            message = f'Pick a task between 0 and {len(command.tasks)}'
            raise(InvalidTaskNumber(message))
        task = command.get(int(task_number))
        command.delete(task)
        if logger:
            logger.info(f'the following task was deleted: {task}')
        print(f'You have deleted task {task}')

    @staticmethod
    def mark_task(options, command, logger=None):
        """ Mark a task as done """
        if logger:
            logger.info(f'user command is {options["option"]}')
        task_number = str(options['task_number'])
        if not task_number.isdigit():
            raise(InvalidTaskNumber('Please pick a number..'))
        if int(task_number) >= len(command.tasks):
            message = f'Pick a task between 0 and {len(command.tasks)}'
            raise(InvalidTaskNumber(message))
        task = command.get(int(task_number))
        if options['task_status'] == 'done':
            task.status = True
        elif options['task_status'] == 'undone':
            task.status = False
        else:
            print("Unknown command.. ")
        if logger:
            message = f'the status of the following task was updated: {task}'
            logger.info(message)

    @staticmethod
    def list_tasks(options, command, logger=None):
        """ Lists all tasks """
        if logger:
            logger.info(f'user command is {options["option"]}')
        TerminalView.task_header()
        TerminalView.display_tasks(command.tasks)
        return True
