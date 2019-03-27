# todocmd.py
# the main file with the entry point

# standard lib imports
import csv
import logging
import os
import sys
from pathlib import Path

# local lib imports
from src import display
from src.command import Command
from src.exception import InvalidOption, InvalidTaskNumber
from src.task import Task


# set the paths
BASEDIR = Path(__file__).parent
LOG_DIR = BASEDIR.joinpath('log')
DATA_DIR = BASEDIR.joinpath('data')
LOG_FILE = BASEDIR.joinpath(LOG_DIR, 'log.txt')
DATA_FILE = BASEDIR.joinpath(DATA_DIR, 'tasks.csv')

# configure the logging module
logging.basicConfig(level=logging.DEBUG,
                    filename=LOG_FILE,
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


def load_tasks(logger=None):
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
    return None


def add_task(user_input, command, logger=None):
    """ Adds a new task in list """
    if logger:
        logger.info(f'user command is {user_input}')
    if user_input == 1:
        task_name = input('Task: ')
        task_note = input('Notes: ')
        start_date = input('Start date (year-month-day): ')
        due_date = input('Due date (year-month-day): ')
       ltask = Task(task_name, task_note, start_date, due_date)
        command.add(task)
        print(f'you have added task: {task}')
        if logger:
            logger.info(f'the following task was added {task}')


def update_task(user_input, command, logger=None):
    """ Updates an existing task """
    if logger:
        logger.info(f'user command is {user_input}')
    if user_input == 2:
        display.prompt()
        display.task_header()
        display.display_tasks(command.tasks)
        try:
            task_number = input('Chose a task >>> ')
            if not task_number.isdigit():
                raise(InvalidTaskNumber('Please pick a number..'))
            if int(task_number) >= len(command.tasks):
                message = f'Pick a task between 0 and {len(command.tasks)}'
                raise(InvalidTaskNumber(message))
            task_name = input('Task name: ')
            task_note = input('Task note: ')
            task_start = input('Start date: ')
            task_due = input('Due date: ')
            task = command.get(len(task_number))
            task.name = task_name
            task.note = task_note
            task.start_date = task_start
            task.end_date = task_due
            command.update(task)
            if logger:
                logger.info(f'the following task was updated {task}')
            display.prompt()
            print(f'You have updated task: {task}')
        except InvalidTaskNumber as e:
            display.prompt()
            print(e)


def delete_task(user_input, command, logger=None):
    """ Delete a task """
     if logger:
        logger.info(f'user command is {user_input}')
    if user_input == 3:
        display.prompt()
        display.task_header()
        display.display_tasks(command.tasks)
        try:
            task_number = input('Chose a task >>> ')
            if not task_number.isdigit():
                raise(InvalidTaskNumber('Please pick a number..'))
            if int(task_number) >= len(command.tasks):
                message = f'Pick a task between 0 and {len(command.tasks)}'
                raise(InvalidTaskNumber(message))
            task = command.get(len(task_number))
            command.delete(task)
            if logger:
                logger.info(f'the following task was deleted: {task}')
            display.prompt()
            print(f'You have deleted task {task}')
        except InvalidTaskNumber as e:
            display.prompt()
            print(e)


def list_tasks(user_input, command, logger=None):
    """ Lists all tasks """
    if logger:
        logger.info(f'user command is {user_input}')
    if user_input == 4:
        display.task_header()
        display.display_tasks(command.tasks)


def save_task(user_input, command, logger=None):
    """ Save task and exit """
    logger.info(f'user command is {user_input}')
    if user_input == 5:
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
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)


# main entry point
def main():

    # STEP 1: define my logger.
    logger = logging.getLogger('todocmd')

    # STEP 2: initiate which will hold the tasks
    command = Command(load_tasks(logger))

    # STEP 4: display the promopt and listen for user input
    display.prompt()

    while True:
        try:
            user_input = display.get_input()

            # Add a new task
            add_task(user_input, command, logger)

            # Update task
            update_task(user_input, command, logger)

            # Delete task
            delete_task(user_input, command, logger)

            # List all tasks
            list_tasks(user_input, command, logger)

            # save and exit app
            save_task(user_input, command, logger)

        except InvalidOption as e:
            display.prompt()
            print(e)


if __name__ == '__main__':
    main()
