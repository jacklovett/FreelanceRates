class RequestModel():
    def __init__(self, form):
        self.salary = form.get('desired-salary', type=int)
        self.billable_hours = form.get('billable-hours', type=int)
        self.time_off = form.get('time-off', type=int) 
        self.has_student_loan = form.get('has-student-loan', type=bool)
        self.plan = self.set_student_loan_plan(form)

    def set_student_loan_plan(self, form):
        plan1 = form.get('plan-1', type=bool)  
        if self.has_student_loan:
            if plan1:
                return 1
            else:
                return 2
        return 0
