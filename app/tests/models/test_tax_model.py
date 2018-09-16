from unittest import TestCase
from app.src.models.tax_model import TaxModel
"""
Test Class for TaxModel
"""
class TestTaxModel(TestCase):    
    
    taxable_income_salary = 12000
    tax_free_amount = 11500

    """
    Test get_taxable_income() returns correct values
    """
    def test_get_taxable_income(self):        
        tax_model = TaxModel(self.taxable_income_salary)
        taxable_income = tax_model.get_taxable_income()
        expected_taxable_income = self.taxable_income_salary - tax_model.tax_free_amount
  
        self.assertEquals(taxable_income, expected_taxable_income)

    """
    Test get_taxable_income() returns 0 when salary is less than
    or equal to tax free amount
    """
    def tax_get_taxable_amount_returns_0(self):
        tax_model = TaxModel(self.tax_free_amount)
        taxable_income = tax_model.get_taxable_income()
        
        self.assertEquals(taxable_income, 0)