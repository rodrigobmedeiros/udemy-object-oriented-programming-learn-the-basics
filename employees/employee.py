from abc import ABC, abstractmethod

class Employee(ABC):

    job_title = 'Generic Job Title'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):

        return f'{self.name}, ${self.salary}, {self.job_title}'

class Manager(Employee):
    job_title = 'Manager'

class Mechanic(Employee):
    job_title = 'Mechanic'
       
class Attendant(Employee):
    job_title = 'Station Attendant'

class Cook(Employee):
    job_title = 'Cook'