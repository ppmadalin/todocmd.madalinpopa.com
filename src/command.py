# command.py
from task import Task


class Command:
    def __init__(self, task_list):
        self.tasks = task_list

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        self._tasks = value

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
