
import re
class RequestModel():
    def __init__(self, form):
        self.salary = self.set_salary(form)
        self.billable_hours = form.get('billable-hours', type=int)
        self.time_off = form.get('time-off', type=int) 
        self.has_student_loan = form.get('has-student-loan', type=bool)
        self.plan = self.set_student_loan_plan(form)
    
    def set_salary(self, form):
        """ 
        Method that removes currency formatting 
        to leave only the float value
        """
        inputSalary = form.get('salary')
        regex = re.compile(r'[^0-9.]+')
        salary = regex.sub('', inputSalary)
        return float(salary)


    def set_student_loan_plan(self, form):
        """
        Handles student loan plan input to determine 
        the selected plan
        """
        plan1 = form.get('plan-1', type=bool)  
        if self.has_student_loan:
            if plan1:
                return 1
            else:
                return 2
        return 0
