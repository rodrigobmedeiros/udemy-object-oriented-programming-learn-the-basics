from abc import ABC, abstractmethod

class BaseReport(ABC):

    def __init__(self, employees):
        self.employees = employees

    @abstractmethod
    def print_report(self):
        pass

class AccountingReport(BaseReport):

    def print_report(self):
        print("Accouting Report")
        print("================")
        for employee in self.employees:
            print(f"{employee.get_full_name()}, {employee.salary}")
        print()

class StaffingReport(BaseReport):

    def print_report(self):
        print("Staffing Report")
        print("===============")
        for employee in self.employees:
            print(f"{employee.get_full_name()}, {employee.job_title}")
        print()