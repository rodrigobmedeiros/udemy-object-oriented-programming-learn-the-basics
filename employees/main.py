from employee import Manager
from employee import Mechanic
from employee import Cook
from employee import Attendant
from employee import Employee

employees = [
    Manager('Vera', 'Schimidt', 2000),
    Attendant("chuck", 'Norris', 1800),
    Attendant('Samantha', 'Carrington', 1800),
    Cook('Roberto', 'Jacketti', 2100),
    Mechanic('Dave', 'DreiBig', 2200),
    Mechanic('Tina', 'River', 2300),
    Mechanic('Ringo', 'Rama', 1900),
    Mechanic('Chuck', 'Rainey', 1900)
]

def print_accouting_report():
    print("Accouting Report")
    print("================")
    for employee in employees:
        print(f"{employee.get_full_name()}, {employee.salary}")
    print()

def print_staffing_report():
    print("Staffing Report")
    print("===============")
    for employee in employees:
        print(f"{employee.get_full_name()}, {employee.job_title}")
    print()

print_accouting_report()

print_staffing_report()
