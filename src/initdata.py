# initdata.py
"""
This modules contains the class which will initiate
the data file
"""
import csv
from pathlib import Path
from src.model.task import Task


class Data:

    @staticmethod
    def load_from_csv_file(DATA_FILE, logger=None):
        """ Loads tasks from a csv file """
        tasks_list = []
        if not Path(DATA_FILE).exists():
            with open(DATA_FILE, mode='w'):
                if logger:
                    logger.debug(f'file: {DATA_FILE} was created')
                return tasks_list
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

    @staticmethod
    def save_to_csv_file(options, command, DATA_FILE, logger=None):
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
            return True
        if logger:
           logger.debug("taks were written")
