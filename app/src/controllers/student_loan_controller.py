from app.src.commons import Commons as commons
class StudentLoanController():
    """
    Student Loan Repayment Class
    """ 
    def __init__(self, salary, plan):
        self.salary = salary
        self.plan = plan
            
    def calc_repayments(self):
        try:
            payment_free_amount = self.get_payment_free_amount()
            if(payment_free_amount > 0):
                return self.get_repayment_amount(payment_free_amount)
            return 0
        except:
            print("A problem occured when calculating repayment amount for plan ", self.plan)
   
    def get_repayment_amount(self, payment_free_amount):
        salaryAboveThreshold = commons.diff_or_zero(self.salary, payment_free_amount)
        return int((salaryAboveThreshold * 0.09) / 12)

    def get_payment_free_amount(self):
        if (self.plan > 0):
            if self.plan == 1:
                return commons.payment_plan1_threshold
            else:
                return commons.payment_plan2_threshold
        return 0