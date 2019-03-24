# todocmd.py
# the main file with the entry point
from pathlib import Path
from task import Task
from command import Command
# from exception import InvalidTaskNumber
import display
import logging
import csv
import sys

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


# main entry point
def main():

    # STEP 1: define my logger.
    logger = logging.getLogger('todocmd')

    # STEP 2: initiate which will hold the tasks
    tasks_list = []

    # STEP 3: create task.csv file and load the tasks in list
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
                    logger.debug(f'tasks were loaded')
                    tasks_list.append(task)

    # STEP 4: initiate commands with the task lists
    command = Command(tasks_list)

    # STEP 5: display the promopt and listen for user input
    display.prompt()
    while True:
        user_input = display.get_input()

        # add task
        if user_input == 1:
            task_name = input('Task: ')
            task_note = input('Notes: ')
            start_date = input('Start date (year-month-day): ')
            due_date = input('Due date (year-month-day): ')
            task = Task(task_name, task_note, start_date, due_date)
            command.add(task)

        # update task
        elif user_input == 2:
            display.task_header()
            display.display_tasks(tasks_list)
            # while True:
            #     try:
            #         task_input = int(input('Chose a task > '))
            #         break
            #     except InvalidTaskNumber:
            #         print('Invalid task number')

        # delete task
        elif user_input == 3:
            pass

        # list all tasks
        elif user_input == 4:
            display.task_header()
            display.display_tasks(tasks_list)

        # save and exit app
        elif user_input == 5:
            with open(DATA_FILE, mode='w', newline="") as f:
                write = csv.writer(f, delimiter=',')
                for task in tasks_list:
                    row = [task.name,
                           task.note,
                           task.start_date,
                           task.end_date,
                           task.status, ]
                    write.writerow(row)
            logger.debug("taks were written")
            sys.exit(0)


if __name__ == '__main__':
    main()
