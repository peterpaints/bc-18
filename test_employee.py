import unittest
from employee import Employee, Manager


class EmployeeClassTest(unittest.TestCase):

    def test_is_employee_instance(self):
        manager = Employee('Zipporah', '123456')
        self.assertIsInstance(manager, Employee, msg='The object should be an instance of the `Employee` class')

    def test_default_employee_experience_level(self):
        manager = Employee('Zipporah', '123456')
        self.assertEqual('junior', manager.experience_level,
                         msg="The employee's experience_level should be called `junior` if no experience_level was passed as an argument")

    def test_default_employee_hourly_rate(self):
        manager = Employee('Zipporah', '123456')
        self.assertEqual(30, manager.hourly_rate, msg="The employee's hourly_rate should be 30 if no hourly_rate was passed as an argument")

    def test_employee_gross_pay(self):
        Recruitment_Manager = Manager('Zipporah', '123456', 'mid_level')
        self.assertEqual(19200, Recruitment_Manager.gross_pay(), msg="The employee's gross_pay is inaccurate")

    def test_employee_net_pay(self):
        Recruitment_Manager = Manager('Zipporah', '123456', 'mid_level')
        self.assertEqual(11520.0, Recruitment_Manager.net_pay(), msg="The employee's net_pay is inaccurate")

    def test_employee_net_pay_is_float(self):
        Recruitment_Manager = Manager('Zipporah', '123456', 'mid_level')
        self.assertTrue(isinstance(Recruitment_Manager.net_pay(), float), msg="The employee's net_pay should be a float")

    def test_vacation_requests(self):
        Engineer = Employee('Peter', '012345', 'mid_level')
        self.assertEqual(17, Engineer.go_on_vacation(5), msg="The employee's vacation_days_left does not reflect the vacation days taken")

    def test_managers_annual_bonus(self):
        Recruitment_Manager = Manager('Zipporah', '123456', 'mid_level')
        self.assertEqual(4608.0, Recruitment_Manager.annual_bonus(90), msg="The employee's annual bonus is inaccurate")

    def test_subclass(self):
        self.assertTrue(issubclass(Manager, Employee), msg="Not true subclass of Employee")

if __name__ == '__main__':
    unittest.main()
