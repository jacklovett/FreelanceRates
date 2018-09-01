# Student Loan Repayment Class
class StudentLoanModel():    
    
    payment_plan1_threshold = 18330
    payment_plan2_threshold = 25000
            
    def get_repayment_amount(self, salary, plan):
        try: 
            payment_free_amount = self.payment_plan1_threshold
            if plan == 2:
                payment_free_amount = self.payment_plan2_threshold 
            repayment_amount = int(((salary - payment_free_amount) * 0.09) / 12)
        except:
            print('A problem occured when calculating repayment amount for plan '+ plan)
        return repayment_amount