import datetime
from abc import ABC, abstractmethod
class BaseShift:

    _start_time: datetime.time
    _end_time: datetime.time

    @property
    def start_time(self):
        return self._start_time
    
    @property
    def end_time(self):
        return self._end_time

    def get_shift_info(self):

        return f'{self.start_time:%H:%M} to {self.end_time:%H:%M}'

class MorningShift(BaseShift):
    _start_time = datetime.time(8, 00)
    _end_time = datetime.time(14, 00)

class AfternoonShift(BaseShift):
    _start_time = datetime.time(12, 00)
    _end_time = datetime.time(20, 00)

class NightShift(BaseShift):
    _start_time = datetime.time(18, 00)
    _end_time = datetime.time(00, 00)
