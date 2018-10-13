from app.src.constants import Constants as constants
# Student Loan Repayment Class
class StudentLoanController():    
    # payment free amounts
    payment_plan1_threshold = 18330
    payment_plan2_threshold = 25000

    def __init__(self, salary, plan):
        self.salary = salary
        self. plan = plan
            
    def calc_repayments(self):
        repayment_amount = 0
        try:
            if self.plan == 1 and self.salary > constants.payment_plan1_threshold:
                repayment_amount = self.get_repayment_amount(constants.payment_plan1_threshold)
            if self.plan == 2 and self.salary > constants.payment_plan2_threshold:
                repayment_amount = self.get_repayment_amount(constants.payment_plan2_threshold)                       
            return repayment_amount
        except:
            print("A problem occured when calculating repayment amount for plan ", self.plan)
   
    def get_repayment_amount(self, payment_free_amount):
        return int(((self.salary - payment_free_amount) * 0.09) / 12)

    def get_payment_free_amount(self):
        if self.plan == 1:
            return constants.payment_plan1_threshold
        else:
            return constants.payment_plan2_threshold