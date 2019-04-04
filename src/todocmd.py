# todocmd.py
# the main file with the entry point

# standard lib imports

# local lib imports
from src.view.termview import TerminalView
from src.exception import InvalidTaskNumber
from src.model.task import Task


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
    task_name = options['task_name']
    task_note = options['task_note']
    task_start = options['task_start']
    task_due = options['task_end']
    task = command.get(int(task_number))
    task.name = task_name
    task.note = task_note
    task.start_date = task_start
    task.end_date = task_due
    command.update(task)
    if logger:
        logger.info(f'the following task was updated {task}')
    print(f'You have updated task: {task}')


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


def list_tasks(options, command, logger=None):
    """ Lists all tasks """
    if logger:
        logger.info(f'user command is {options["option"]}')
    TerminalView.task_header()
    TerminalView.display_tasks(command.tasks)
    return True
