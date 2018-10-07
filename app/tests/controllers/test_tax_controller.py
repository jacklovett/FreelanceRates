from unittest import TestCase, mock
from unittest.mock import patch
from app.src.controllers.tax_controller import TaxController

class TestTaxController(TestCase):    
    """
    Test Class for TaxController - 
    Review salaries used for objects. get_tax_amount uses taxable income, not salary
    """
    taxable_income_salary = 12000
    tax_free_amount = 11500 # use constants class
    # use constants for these
    basic_amount = 33500 # basic boundary
    higher_amount = 150000 + tax_free_amount # higher boundary
    additional_rate_amount = 150000 + tax_free_amount + 1 # higher boundary + 1

    basic_tax_ctrl = TaxController(basic_amount)
    higher_tax_ctrl = TaxController(higher_amount)
    additional_rate_tax_ctrl = TaxController(additional_rate_amount)    

    @patch.object(basic_tax_ctrl, 'basic_rate')
    def test_get_tax_amount_basic_rate(self, mock):
        """
        Test get_tax_amount() returns correct value
        when taxable income fits the basic rate
        """    
        tax_amount = self.basic_tax_ctrl.get_tax_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(tax_amount, None)
        self.assertEquals(tax_amount, self.basic_tax_ctrl.basic_rate())

    @patch.object(higher_tax_ctrl, 'higher_rate')
    def test_get_tax_amount_higher_rate(self, mock):
        """
        Test get_tax_amount() returns correct value
        when taxable income exceeds the higher rate
        """
        tax_amount = self.higher_tax_ctrl.get_tax_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(tax_amount, None)
        self.assertEquals(tax_amount, self.higher_tax_ctrl.higher_rate())

    @patch.object(additional_rate_tax_ctrl, 'additional_rate')
    def test_get_tax_amount_additional_rate(self, mock):
        """
        Test get_tax_amount() returns correct value
        when taxable income exceeds the additional higher rate
        """
        tax_amount = self.additional_rate_tax_ctrl.get_tax_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(tax_amount, None)
        self.assertEquals(tax_amount, self.additional_rate_tax_ctrl.additional_rate())

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

    def test_basic_rate(self):
        """
        Test basic rate calculation
        """
        taxable_income = self.basic_tax_ctrl.taxable_income
        basic_rate = self.basic_tax_ctrl.basic_rate()
        self.assertIsNotNone(basic_rate)
        self.assertEquals(basic_rate, taxable_income * 0.2)

    @patch.object(higher_tax_ctrl, 'basic_rate')
    def test_higher_rate(self, mock):
        """
        Test higher rate calculation
        """
        higher_rate = self.higher_tax_ctrl.higher_rate()
        self.assertTrue(mock.called)
        self.assertNotEquals(higher_rate, None)

    @patch.object(additional_rate_tax_ctrl, 'higher_rate')
    def test_additional_rate(self, mock):
        """
        Test additional rate calculation
        """
        additional_rate = self.additional_rate_tax_ctrl.additional_rate()
        self.assertTrue(mock.called)
        self.assertNotEquals(additional_rate, None)
        
