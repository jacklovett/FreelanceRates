class MainController():
    def __init__(self, form):
        self.form = form
        self.desired_salary = form.get('desired_salary', type=int)
        self.billable_hours = form.get('billable_hours', type=int)
        self.time_off = form.get('time_off', type=int)
        self.student_loan_plan = self.determine_student_loan_plan()        
        
    def calc_result(self):
        print(self.form.get('desired_salary'))
    
    def determine_student_loan_plan(self):
        input_form = self.form
        has_student_loan = input_form.get('plan_toggle', type=bool)
        if has_student_loan == 'on':
            if input_form.get('plan_1', type=bool) == 'on':
                return 1            
            if input_form.get('plan_2', type=bool) == 'on':
                return 2        
        else:
            return 0


