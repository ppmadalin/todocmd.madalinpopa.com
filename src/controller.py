# command.py
""" This module holds all the supported commands over a task """

from argparse import ArgumentParser
from src.models import Task


class CommandLine(ArgumentParser):

    def __init__(self):
        super().__init__()
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
                          dest='task',
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


class Command:

    supported_commands = {
        1: 'Add task',
        2: 'Edit task',
        3: 'Delete task',
        4: 'List all tasks',
        5: 'Save/Exit',
    }

    def __init__(self, task_list):
        self.__tasks = task_list

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, value):
        self.__tasks = value

    def add(self, task):
        """ add a task in tasks """
        if isinstance(task, Task):
            self.tasks.append(task)
            return task
        return False

    def get(self, index):
        """ returns a task """
        return self.tasks[index]

    def update(self, task):
        """ update a task """
        for tk in self.tasks:
            if tk.id == task.id:
                index = self.tasks.index(tk)
                self.tasks[index] = task
                return tk
        return None

    def delete(self, task):
        """ delete a task """
        for tk in self.tasks:
            if tk.id == task.id:
                self.tasks.remove(tk)
                return tk
        return None
