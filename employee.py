class Employee(object):
    def __init__(self, name, payroll_number, experience_level='junior'):
        self.name = name
        self.payroll_number = payroll_number
        self.experience_level = experience_level
        self.hourly_rate = 30 if experience_level == 'junior' else 60 if experience_level == 'mid_level' else 100
        self.vacation_days_left = 22

    def gross_pay(self, hours_worked=160):
        self.hours_worked = hours_worked
        return self.hours_worked * self.hourly_rate

    def net_pay(self, tax_bracket=0):
        tax_bracket = 0.2 if self.hourly_rate < 60 else 0.3 if self.hourly_rate == 60 else 0.4
        gross = self.gross_pay()
        self.tax_bracket = tax_bracket
        return gross - (self.tax_bracket * gross)

    def go_on_vacation(self, request):
        self.vacation_days_left -= request
        return self.vacation_days_left


class Manager(Employee):
    def __init__(self, name, payroll_number, experience_level='junior'):
        super(Manager, self).__init__(name, payroll_number, experience_level)
        self.hourly_rate = 60 if experience_level == 'junior' else 120 if experience_level == 'mid_level' else 200
        self.vacation_days_left = 30

    def annual_bonus(self, teams_performance, bonus_rate=0):
        if teams_performance < 50:
            bonus_rate = 0
        elif teams_performance < 60:
            bonus_rate = 0.1
        elif teams_performance < 70:
            bonus_rate = 0.2
        elif teams_performance < 80:
            bonus_rate = 0.3
        else:
            bonus_rate = 0.4
        self.bonus_rate = bonus_rate
        self.annual_bonus = self.net_pay() * self.bonus_rate
        return self.annual_bonus


# Engineer = Employee('Peter', '012345', 'mid_level')
# Recruitment_Manager = Manager('Zipporah', '123456', 'mid_level')
# print Engineer.net_pay()
# print Recruitment_Manager.annual_bonus(79)
# print Recruitment_Manager.experience_level
