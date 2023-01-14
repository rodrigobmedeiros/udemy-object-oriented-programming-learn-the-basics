from employees.employee import Manager
from employees.employee import Mechanic
from employees.employee import Cook
from employees.employee import Attendant

from reports.reports import AccountingReport
from reports.reports import StaffingReport

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

accouting_report = AccountingReport(employees)
staffing_report = StaffingReport(employees)

accouting_report.print_report()
staffing_report.print_report()
