# task.py


class Task:
    def __init__(self, name, note, start_date, end_date, status):
        self.name = name
        self.note = note
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        self._note = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
