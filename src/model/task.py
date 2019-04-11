# task.py
"""
This modules contains the Task object.

"""
import uuid


class Task:

    _name: str
    _note: str
    _start_date: str
    _end_date: str
    _status: str
    _id: str

    def __init__(self,
                 name,
                 note=None,
                 start_date=None,
                 end_date=None,
                 status=False):

        self._name = name
        self._note = note
        self._start_date = start_date
        self._end_date = end_date
        self._status = status
        self._id = str(uuid.uuid4())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def note(self) -> str:
        return self._note

    @note.setter
    def note(self, value: str):
        self._note = value

    @property
    def start_date(self) -> str:
        return self._start_date

    @start_date.setter
    def start_date(self, value: str):
        self._start_date = value

    @property
    def end_date(self) -> str:
        return self._end_date

    @end_date.setter
    def end_date(self, value: str):
        self._end_date = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value

    @property
    def id(self) -> str:
        return self._id

    def __str__(self) -> str:
        return f'{self._name}'

    def __repr__(self) -> str:
        return f'{self._name}: {self._id}'
