from app.src.commons import Commons as commons
class TaxController():
    """
    Tax Calculations Class
    """    
    def __init__(self, salary):
        self.salary = salary

    def get_tax_amount(self):
        try:
            if self.salary <= commons.higher_rate_threshold:
                return self.basic_rate()
            elif commons.higher_rate_threshold < self.salary <= commons.additional_rate_threshold:
                return self.higher_rate()
            else:
                return self.additional_rate() 
        except:
            print("A problem occured when calculating the amount of tax to pay.")

    def basic_rate(self):
        if self.salary > commons.higher_rate_threshold:
            basic_amount = (commons.higher_rate_threshold) * 0.2
            return basic_amount
        return self.get_taxable_income() * 0.2

    def higher_rate(self):
        if self.salary > commons.additional_rate_threshold:
            higher_amount = (commons.additional_rate_threshold - commons.higher_rate_threshold) * 0.4
            return higher_amount

        higher_amount = (self.salary - commons.higher_rate_threshold) * 0.4
        return higher_amount + self.basic_rate()

    def additional_rate(self):
        additional_amount = (self.salary - commons.additional_rate_threshold) * 0.45
        return additional_amount + self.higher_rate() + self.basic_rate()
     
    def get_taxable_income(self):
        return commons.diff_or_zero(self.salary, commons.tax_free_amount)

    def get_income_after_tax(self):
        return commons.diff_or_zero(self.salary, self.get_tax_amount())   