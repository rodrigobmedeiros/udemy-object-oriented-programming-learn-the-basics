from employees.employee import Manager
from employees.employee import Mechanic
from employees.employee import Cook
from employees.employee import Attendant

from reports.reports import AccountingReport
from reports.reports import StaffingReport
from reports.reports import SchedulingReport

from shift.shift import MorningShift
from shift.shift import AfternoonShift
from shift.shift import NightShift

employees = [
    Manager('Vera', 'Schimidt', 2000, MorningShift()),
    Attendant("chuck", 'Norris', 1800, MorningShift()),
    Attendant('Samantha', 'Carrington', 1800, AfternoonShift()),
    Cook('Roberto', 'Jacketti', 2100, AfternoonShift()),
    Mechanic('Dave', 'DreiBig', 2200, MorningShift()),
    Mechanic('Tina', 'River', 2300, AfternoonShift()),
    Mechanic('Ringo', 'Rama', 1900, AfternoonShift()),
    Mechanic('Chuck', 'Rainey', 1900, NightShift())
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    SchedulingReport(employees)
]


for report in reports:
    report.print_report()
