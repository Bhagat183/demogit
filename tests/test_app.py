from app import get_employees


def test_every_employee_has_email():
    employees = get_employees()

    for employee in employees:
        assert "email" in employee