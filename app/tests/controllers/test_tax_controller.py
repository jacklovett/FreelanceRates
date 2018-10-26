from unittest import TestCase, mock
from unittest.mock import patch
from app.src.commons import Commons as commons
from app.src.controllers.tax_controller import TaxController

class TestTaxController(TestCase):    
    """
    Test Class for TaxController 
    """
    taxable_income_salary = 12000
    higher_amount = 52000
    additional_rate_amount = 150008

    zero_tax_ctrl = TaxController(1)
    tax_ctrl = TaxController(taxable_income_salary)
    higher_tax_ctrl = TaxController(higher_amount)
    additional_rate_tax_ctrl = TaxController(additional_rate_amount)   
    
    def test_get_tax_amount_basic_rate(self):
        """
        Test get_tax_amount() returns correct value
        when taxable income fits the basic rate
        """    
        tax_ctrl = TaxController(self.taxable_income_salary)
        tax_amount = tax_ctrl.get_tax_amount()
        self.assertIsNotNone(tax_amount)
        self.assertEqual(tax_amount, tax_ctrl.basic_rate())
    
    def test_get_tax_amount_higher_rate(self):
        """
        Test get_tax_amount() returns correct value
        when taxable income exceeds the higher rate
        """
        higher_tax_ctrl = TaxController(self.higher_amount)
        tax_amount = higher_tax_ctrl.get_tax_amount()
        self.assertIsNotNone(tax_amount)
        self.assertEqual(tax_amount, higher_tax_ctrl.higher_rate())

    def test_get_tax_amount_additional_rate(self):
        """
        Test get_tax_amount() returns correct value
        when taxable income exceeds the additional higher rate
        """
        tax_amount = self.additional_rate_tax_ctrl.get_tax_amount()
        self.assertIsNotNone(tax_amount)
        self.assertEqual(tax_amount, self.additional_rate_tax_ctrl.additional_rate())
    
    def test_basic_rate(self):
        """
        Test basic_rate() returns correct value
        when salary is greater than tax free amount but less than
        the higher rate threshold.
        """
        basic_rate_amount = self.tax_ctrl.basic_rate()
        self.assertIsNotNone(basic_rate_amount)
        self.assertEqual(basic_rate_amount, 30.00)

    def test_higher_rate(self):
        """
        Test higher_rate() returns correct value
        when salary is greater than the higher threshold
        rate but less than the additional threshold rate.
        """
        higher_rate_amount = self.higher_tax_ctrl.higher_rate()
        self.assertIsNotNone(higher_rate_amount)
        self.assertEqual(higher_rate_amount, 9160.00)

    def test_additional_rate(self):
        """
        Test additional_rate() returns correct value 
        when salary is greater than the additional rate
        threshold rate.
        """
        additional_rate_amount = self.additional_rate_tax_ctrl.additional_rate()
        self.assertIsNotNone(additional_rate_amount)
        self.assertEqual(additional_rate_amount, 53103.60)

    def test_get_taxable_income(self):
        """
        Test get_taxable_income() returns correct values
        """        
        taxable_income = self.tax_ctrl.get_taxable_income()
        expected_taxable_income = self.taxable_income_salary - commons.tax_free_amount
        self.assertIsNotNone(taxable_income)
        self.assertEqual(taxable_income, expected_taxable_income)
    
    def test_get_taxable_income_returns_0(self):
        """
        Test get_taxable_income() returns 0 when salary is less than
        or equal to tax free amount
        """
        taxable_income = self.zero_tax_ctrl.get_taxable_income()
        self.assertIsNotNone(taxable_income)
        self.assertEqual(taxable_income, 0)

    def test_get_income_after_tax(self):
        """
        Test get_income_after_tax() returns correct values
        """        
        income = self.tax_ctrl.get_income_after_tax()
        expected_income = self.taxable_income_salary - self.tax_ctrl.get_tax_amount()
        self.assertIsNotNone(income)
        self.assertEqual(income, expected_income)

    def test_get_income_after_tax_when_taxable_income_0(self):
        """
        Test get_income_after_tax() returns taxable income equals 0
        Should return same amount as the salary
        """        
        income = self.zero_tax_ctrl.get_income_after_tax()
        self.assertIsNotNone(income)
        self.assertEqual(income, self.zero_tax_ctrl.salary)

    def test_get_amount_throws_execption(self):
        """
        Test that get_tax_amout() handles exceptions
        """
        self.tax_ctrl.salary = None
        self.assertRaises(Exception, self.tax_ctrl.get_tax_amount())     
