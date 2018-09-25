from tax_controller import TaxController
from nic_controller import NicController
from student_loan_controller import StudentLoanController

class MainController():   
    """
    MainController Class
    The main class that will take the users input, perform the 
    necessary calculations and then return the result back to the 
    front end
    """
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

        tax_ctrl = TaxController(self.salary)
        profit = tax_ctrl.get_income_after_tax() 
        self.calc_nic_results(profit)
       
        if self.has_student_loan:
            self.calc_student_loan_results()

        return self.result
     
    def calc_nic_results(self, profit):
        nic_ctrl = NicController(profit)
        self.result['nic_class'] = nic_ctrl.get_nic_class()
        self.result['nic_amount'] = nic_ctrl.get_nic_amount()

    def calc_student_loan_results(self):
        student_loan_ctrl = StudentLoanController(self.salary, self.plan)
        self.result['has-student-loan'] = self.has_student_loan
        self.result['student-loan-plan'] = self.plan
        self.result['payment_free_amount'] = student_loan_ctrl.get_payment_free_amount()
        self.result['student-loan-repayments'] = student_loan_ctrl.calc_repayments()