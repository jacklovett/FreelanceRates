class MainController():
    def __init__(self, form):
        self.form = form
        self.desired_salary = form.get('desired_salary', type=int)
        self.billable_hours = form.get('billable_hours', type=int)
        self.time_off = form.get('time_off', type=int)
        self.student_loan_plan = self.determine_student_loan_plan(form)        
        
    def calc_result(self):
        result = {}
        result['desired_salary'] = self.form.get('desired_salary')
        result['billable_hours'] = self.form.get('billable_hours')
        result['time_off'] = self.form.get('time_off')
        result['student_loan_plan'] = self.student_loan_plan
        return result
    
    def determine_student_loan_plan(self, form):
        has_student_loan = form.get('plan_toggle', type=bool)
        if has_student_loan:
            if form.get('plan_1', type=bool):
                return 1            
            if form.get('plan_2', type=bool):
                return 2        
        else:
            return 0


