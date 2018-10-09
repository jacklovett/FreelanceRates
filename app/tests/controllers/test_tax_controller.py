from unittest import TestCase, mock
from unittest.mock import patch
from app.src.controllers.tax_controller import TaxController
from app.src.constants import Constants as constants

class TestTaxController(TestCase):    
    """
    Test Class for TaxController - 
    Review salaries used for objects. get_tax_amount uses taxable income, not salary
    """
    taxable_income_salary = 12000
    higher_amount = constants.higher + constants.tax_free_amount # higher boundary
    additional_rate_amount = constants.higher + constants.tax_free_amount + 1 # higher boundary + 1

    zero_tax_ctrl = TaxController(1)
    tax_ctrl = TaxController(taxable_income_salary)
    basic_tax_ctrl = TaxController(constants.basic)
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
        taxable_income = self.tax_ctrl.get_taxable_income()
        expected_taxable_income = self.taxable_income_salary - constants.tax_free_amount
        self.assertIsNotNone(taxable_income)
        self.assertEquals(taxable_income, expected_taxable_income)
    
    def test_get_taxable_amount_returns_0(self):
        """
        Test get_taxable_income() returns 0 when salary is less than
        or equal to tax free amount
        """
        taxable_income = self.zero_tax_ctrl.get_taxable_income()
        self.assertIsNotNone(taxable_income)
        self.assertEquals(taxable_income, 0)

    def test_get_income_after_tax(self):
        """
        Test get_income_after_tax() returns correct values
        """        
        income = self.tax_ctrl.get_income_after_tax()
        expected_income = self.taxable_income_salary - self.tax_ctrl.tax_amount
        self.assertIsNotNone(income)
        self.assertEquals(income, expected_income)

    def test_get_income_after_tax_returns_0(self):
        """
        Test get_income_after_tax() returns 0 when salary is less than
        or equal to tax amount
        """        
        taxable_income = self.zero_tax_ctrl.get_taxable_income()
        self.assertIsNotNone(taxable_income)
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

    def test_diff_or_zero(self):
        """
        Test diff_or_zero calculation
        """
        diff_result = self.tax_ctrl.diff_or_zero(2,1)
        zero_result = self.tax_ctrl.diff_or_zero(1,2)
        self.assertEquals(diff_result, 1)
        self.assertEquals(zero_result, 0)
        
