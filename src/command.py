# command.py


class Command:
    def __init__(self, task_list):
        self.tasks = task_list

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        self._tasks = value

    def add_task(self, task):
        return task
