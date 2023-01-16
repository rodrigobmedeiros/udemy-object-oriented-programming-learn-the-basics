from employees.employee import (
    Employee
)


def test_get_employee_full_name():
    vera = Employee('Vera', 'Schimidt', 0, None)

    assert vera.get_full_name() == 'Vera Schimidt'

def test_raise_salary():
    employee = Employee('', '', 2000, None)
    amount = 500
    employee.raise_salary(amount)

    assert employee.salary == 2500