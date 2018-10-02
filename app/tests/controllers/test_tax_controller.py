from unittest import TestCase
from app.src.controllers.tax_controller import TaxController

class TestTaxController(TestCase):    
    """
    Test Class for TaxController
    """
    taxable_income_salary = 12000
    tax_free_amount = 11500
    
    def test_get_taxable_income(self):
        """
        Test get_taxable_income() returns correct values
        """        
        tax_controller = TaxController(self.taxable_income_salary)
        taxable_income = tax_controller.get_taxable_income()
        expected_taxable_income = self.taxable_income_salary - tax_controller.tax_free_amount
  
        self.assertEquals(taxable_income, expected_taxable_income)
    
    def test_get_taxable_amount_returns_0(self):
        """
        Test get_taxable_income() returns 0 when salary is less than
        or equal to tax free amount
        """
        tax_controller = TaxController(self.tax_free_amount)
        taxable_income = tax_controller.get_taxable_income()
        
        self.assertEquals(taxable_income, 0)