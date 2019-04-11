# main.py
# main entry point

# standard lib imports
import logging
import sys
from pathlib import Path

# local lib imports
from src.view.termview import TerminalView
from src.controller.basectrl import BaseController
from src.cmdargs import CommandArgs
from src.initdata import Data
from src.exception import InvalidOption, InvalidTaskNumber
from src.controller.termctrl import TerminalController

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
                TerminalController.add_task(options, command, logger)

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
                TerminalController.update_task(options, command, logger)

            # Delete task
            if user_input == 3:
                options['option'] = user_input
                options['task_number'] = input('Task number >>> ')
                TerminalController.delete_task(options, command, logger)

            # List all tasks
            if user_input == 4:
                options['option'] = user_input
                TerminalView.prompt()
                print()  # add a space
                TerminalController.list_tasks(options, command, logger)

            # save and exit app
            if user_input == 5:
                options['option'] = user_input
                Data.save_to_csv_file(options, command, DATA_FILE, logger)
                sys.exit(0)

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
    cmd = CommandArgs(DATA_FILE)

    # STEP 4: parse args
    args = cmd.parse_args()

    # START INTERFACE
    if args.interactive:
        interface()

    # LIST TASKS
    cmd.list_tasks(TerminalController, command, logger)

    # ADD NEW TASK
    cmd.add_task(TerminalController, command, logger)

    # DELETE TASK
    cmd.delete_task(TerminalController, command, logger)

    # UPDATE TASK
    cmd.delete_task(TerminalController, command, logger)

    # UPDATE TASK NAME
    cmd.update_task_name(TerminalController, command, logger)


if __name__ == '__main__':
    main()
