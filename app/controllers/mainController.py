from taxModel import TaxModel
from nicModel import NicModel
from studentLoanModel import StudentLoanModel

class MainController():     
    def __init__(self, request):
        self.salary = request.salary
        self.billable_hours = request.billable_hours
        self.time_off = request.time_off
        self.has_student_loan = request.has_student_loan
        self.plan = request.plan

    def calc_result(self):
         
        result = {}
        result['salary'] = self.salary
        result['billable-hours'] = self.billable_hours
        result['time-off'] = self.time_off
        result['has-student-loan'] = self.has_student_loan
       
        if self.has_student_loan:
            student_loan_model = StudentLoanModel()
            result['student-loan-plan'] = self.plan
            result['payment_free_amount'] = student_loan_model.get_payment_free_amount(self.plan)
            result['student-loan-repayments'] = student_loan_model.calc_repayments(self.salary, self.plan)

        return result

            


