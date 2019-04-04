# main.py
# main entry point

# standard lib imports
import logging
from pathlib import Path

# local lib imports
from src.view.termview import TerminalView
from src.controller.basectrl import BaseController
from src.cmdargs import CommandArgs
from src.initdata import Data
from src.exception import InvalidOption, InvalidTaskNumber
from src.controller.termctrl import (add_task, delete_task, list_tasks,
                                     update_task)


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


def interface():
    """ Main entry point """

    # STEP 1: define my logger.
    logger = logging.getLogger('todocmd')

    # STEP 2: initiate which will hold the tasks
    command = BaseController(Data.load_from_csv_file(DATA_FILE, logger))

    # STEP 4: views the promopt and listen for user input
    TerminalView.prompt()

    while True:
        try:
            # input
            user_input = TerminalView.get_input()

            # options
            options = {}

            # Add a new task
            if user_input == 1:
                options['option'] = user_input
                options['task_name'] = input('Task: ')
                options['task_note'] = input('Note: ')
                options['task_start'] = input('Start date: ')
                options['task_end'] = input('Due date: ')
                TerminalView.prompt()
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
                TerminalView.prompt()
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
                TerminalView.prompt()
                print()  # add a space
                list_tasks(options, command, logger)

            # save and exit app
            if user_input == 5:
                options['option'] = user_input
                Data.save_to_csv_file(options, command, DATA_FILE, logger)

        except InvalidOption as e:
            TerminalView.prompt()
            print()  # add a space
            print(e)
        except InvalidTaskNumber as e:
            TerminalView.prompt()
            print()  # add a space
            print(e)


def main():
    """ Command Line args """

    # STEP 1: define my logger.
    logger = logging.getLogger('todocmd')

    # STEP 2: initiate which will hold the tasks
    command = BaseController(Data.load_from_csv_file(DATA_FILE, logger))

    # STEP 3: initiate command line args
    cmd = CommandArgs()

    # STEP 4: parse args
    args = cmd.parse_args()

    # options
    options = {}

    # START INTERFACE
    if args.interactive:
        interface()

    # LIST TASKS
    if args.tasks:
        options['option'] = '-l --list'
        list_tasks(options, command, logger)

    # ADD NEW TASK
    if args.add:
        options['option'] = '--add'
        options['task_name'] = args.add[0]
        options['task_note'] = args.add[1]
        options['task_start'] = args.add[2]
        options['task_end'] = args.add[3]

        # add task
        add_task(options, command, logger)

        # save changes
        Data.save_to_csv_file(options, command, DATA_FILE, logger)

    # DELETE TASK
    if args.delete:
        options['option'] = '--delete'
        options['task_number'] = args.delete[0]

        # delete task
        delete_task(options, command, logger)

        # save change
        Data.save_to_csv_file(options, command, DATA_FILE, logger)

    # UPDATE TASK
    if args.task and args.update:
        options['option'] = '-u'
        options['task_number'] = args.task[0]
        options['task_name'] = args.update[0]
        options['task_note'] = args.update[1]
        options['task_start'] = args.update[2]
        options['task_end'] = args.update[3]

        # update task
        update_task(options, command, logger)

        # save change
        Data.save_to_csv_file(options, command, DATA_FILE, logger)


if __name__ == '__main__':
    main()
