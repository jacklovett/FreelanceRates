# Student Loan Repayment Class
class StudentLoanModel():    
    
    payment_plan1_threshold = 18330
    payment_plan2_threshold = 25000
            
    def calc_repayments(self, salary, plan):
        repayment_amount = 0
        try:
            if plan == 1 and salary > self.payment_plan1_threshold:
                repayment_amount = self.get_repayment_amount(salary, self.payment_plan1_threshold) 

            if plan == 2 and salary > self.payment_plan2_threshold:
                repayment_amount = self.get_repayment_amount(salary, self.payment_plan2_threshold)
                       
            return repayment_amount
        except:
            print("A problem occured when calculating repayment amount for plan ", plan)
   
    def get_repayment_amount(self, salary, payment_free_amount):
        return int(((salary - payment_free_amount) * 0.09) / 12)

    def get_payment_free_amount(self, plan):
        if plan == 1:
            return self.payment_plan1_threshold
        else:
            return self.payment_plan2_threshold

