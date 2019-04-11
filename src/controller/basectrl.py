# basectrl.py
"""
Base Controller is the module where all the basic
command are defined.

Some examples of these comands are the following:

    - add(task)
    - delete(task)
    - update(task)
"""

from src.model.task import Task


class BaseController:

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
