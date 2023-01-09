from employee import Manager
from employee import Mechanic
from employee import Cook
from employee import Attendant
from employee import Employee

employees = [
    Manager('Vera', 2000),
    Attendant("chuck", 1800),
    Attendant('Samantha', 1800),
    Cook('Roberto', 2100),
    Mechanic('Dave', 2200),
    Mechanic('Tina', 2300),
    Mechanic('Ringo', 1900)
]

for employee in employees:
    print(employee)


employee = Employee('Rodrigo', 2000)
print(employee)