# todocmd.py
# the main file with the entry point

# standard lib imports
import csv
import sys

# local lib imports
from pathlib import Path
from src import display
from src.exception import InvalidTaskNumber
from src.task import Task


def load_tasks(DATA_FILE, logger=None):
    """ Loads task and create the tasks.csv file if not exists """
    tasks_list = []
    if not Path(DATA_FILE).exists():
        with open(DATA_FILE, mode='w'):
            logger.debug(f'file: {DATA_FILE} was created')
            pass
    else:
        with open(DATA_FILE, mode='r', newline="") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if len(row) > 4:
                    task = Task(row[0],
                                row[1],
                                row[2],
                                row[3],
                                row[4],)
                    if logger:
                        logger.debug(f'tasks were loaded')
                    tasks_list.append(task)
            return tasks_list


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
    display.task_header()
    display.display_tasks(command.tasks)
    return True


def save_task(options, command, DATA_FILE, logger=None):
    """ Save task and exit """
    if logger:
        logger.info(f'user command is {options["option"]}')
    with open(DATA_FILE, mode='w', newline="") as f:
        write = csv.writer(f, delimiter=',')
        for task in command.tasks:
            row = [task.name,
                   task.note,
                   task.start_date,
                   task.end_date,
                   task.status, ]
            write.writerow(row)
    if logger:
        logger.debug("taks were written")
    sys.exit(0)
