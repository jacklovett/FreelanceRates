from tax_model import TaxModel
from nic_model import NicModel
from student_loan_model import StudentLoanModel

class MainController():   
    
    result = {}

    def __init__(self, request):
        self.salary = request.salary
        self.billable_hours = request.billable_hours
        self.time_off = request.time_off
        self.has_student_loan = request.has_student_loan
        self.plan = request.plan

    def calc_result(self):
                
        self.result['salary'] = self.salary
        self.result['billable-hours'] = self.billable_hours
        self.result['time-off'] = self.time_off

        tax_model = TaxModel(self.salary)
        profit = tax_model.get_income_after_tax() 
        self.calc_nic_results(profit)
       
        if self.has_student_loan:
            self.calc_student_loan_results()

        return self.result
       
    
    def calc_nic_results(self, profit):
        nic_model = NicModel(profit)
        self.result['nic_class'] = nic_model.get_nic_class()
        self.result['nic_amount'] = nic_model.get_nic_amount()

    def calc_student_loan_results(self):
        student_loan_model = StudentLoanModel(self.salary, self.plan)
        self.result['student-loan-plan'] = self.plan
        self.result['payment_free_amount'] = student_loan_model.get_payment_free_amount()
        self.result['student-loan-repayments'] = student_loan_model.calc_repayments()

            


