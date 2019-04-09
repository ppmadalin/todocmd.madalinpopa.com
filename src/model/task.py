# task.py
import uuid
from typing import *


class Task:

    _name: str
    _note: str

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
    def name(self, value: List[str]):
        self._name = value

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f'{self.__name}: {self.__id}'
