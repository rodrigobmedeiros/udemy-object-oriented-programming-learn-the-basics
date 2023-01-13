from abc import ABC, abstractmethod

class Employee(ABC):

    job_title = 'Generic Job Title'

    def __init__(self, first_name, last_name,  salary):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary

    def __str__(self):

        return f'{self._first_name}, ${self.salary}, {self.job_title}'

    def get_full_name(self):

        return f"{self._first_name} {self._last_name}"

class Manager(Employee):
    job_title = 'Manager'

class Mechanic(Employee):
    job_title = 'Mechanic'
       
class Attendant(Employee):
    job_title = 'Station Attendant'

class Cook(Employee):
    job_title = 'Cook'