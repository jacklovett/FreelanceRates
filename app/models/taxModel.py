# Tax Class
class TaxModel():
    def __init__(self, salary):
        self.tax_free = 11500
        # Boundaries
        self.basic = 33500
        self.higher = 150000
        self.taxable_income = salary - self.tax_free
        self.tax_amount = self.set_tax_amount()
        self.income_after_tax = salary - self.tax_amount               
 
    def set_tax_amount(self):
        if self.basic <= self.taxable_income <= self.higher:
            return self.higher_rate()
        elif self.taxable_income > self.higher:
            return self.additional_rate() 
        else:
            return self.basic_rate()
          
    def basic_rate(self):
        if self.taxable_income < self.basic:
            return self.taxable_income * 0.2
        else:
            return self.basic * 0.2
        
    def higher_rate(self):
        amount_above_basic_rate = self.taxable_income - self.basic
        higher_rate_amount = amount_above_basic_rate * 0.4
        return self.basic_rate() + higher_rate_amount
        
    def additional_rate(self):
        amount_above_additional_rate = self.taxable_income - self.higher
        additional_rate_amount = amount_above_additional_rate * 0.45
        return self.higher_rate() + additional_rate_amount  
