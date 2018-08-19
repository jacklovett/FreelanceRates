# Student Loan Repayment Class
class student_loan_model():    
    def __init__(self, salary, plan):
        self.salary = salary 
        self.plan = plan
        self.repayment_amount = self.set_repayment() 
  
    def set_repayment(self):
        if  self.plan == 1:
            payment_free_amount = 17775
            return (self.salary - payment_free_amount) * 0.09
        else:
            return 100 # look into plan 2 calculation