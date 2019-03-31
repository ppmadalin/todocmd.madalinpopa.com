# main.py
# main entry point

# standard lib imports
import logging
from pathlib import Path

# local lib imports
from src import display
from src.command import Command
from src.exception import InvalidOption, InvalidTaskNumber
from src.todocmd import (add_task, delete_task, list_tasks,
                         load_tasks, save_task, update_task)


# set the paths
BASEDIR = Path(__file__).parent
LOG_DIR = BASEDIR.joinpath('log')
DATA_DIR = BASEDIR.joinpath('data')
LOG_FILE = BASEDIR.joinpath(LOG_DIR, 'log.txt')
DATA_FILE = BASEDIR.joinpath(DATA_DIR, 'tasks.csv')

# configure the lo?!?jedi=0, gging module?!? (*_***kwargs*_*) ?!?jedi?!?
logging.basicConfig(level=logging.DEBUG,
                    filename=LOG_FILE,
                    filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


def main():

    # STEP 1: define my logger.
    logger = logging.getLogger('todocmd')

    # STEP 2: initiate which will hold the tasks
    command = Command(load_tasks(DATA_FILE, logger))

    # STEP 4: display the promopt and listen for user input
    display.prompt()

    while True:
        try:
            # input
            user_input = display.get_input()

            # options
            options = {}

            # Add a new task
            if user_input == 1:
                options['option'] = user_input
                options['task_name'] = input('Task: ')
                options['task_note'] = input('Note: ')
                options['task_start'] = input('Start date: ')
                options['task_end'] = input('Due date: ')
                display.prompt()
                print()  # add a space
                add_task(options, command, logger)

            # Update task
            if user_input == 2:
                options['option'] = user_input
                options['task_number'] = input('Task number >>> ')
                options['task_name'] = input('Task: ')
                options['task_note'] = input('Note: ')
                options['task_start'] = input('Start date: ')
                options['task_end'] = input('Due date: ')
                display.prompt()
                print()  # add a space
                update_task(options, command, logger)

            # Delete task
            if user_input == 3:
                options['option'] = user_input
                options['task_number'] = input('Task number >>> ')
                delete_task(options, command, logger)

            # List all tasks
            if user_input == 4:
                options['option'] = user_input
                display.prompt()
                print()  # add a space
                list_tasks(options, command, logger)

            # save and exit app
            if user_input == 5:
                options['option'] = user_input
                save_task(options, command, DATA_FILE, logger)

        except InvalidOption as e:
            display.prompt()
            print()  # add a space
            print(e)
        except InvalidTaskNumber as e:
            display.prompt()
            print()  # add a space
            print(e)


if __name__ == '__main__':
    main()
