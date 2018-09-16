from unittest import TestCase, mock
from unittest.mock import patch
from app.src.models.nic_model import NicModel

class TestNicModel(TestCase):
    """
    Test Class for NicModel
    """
     # Class Thresholds
    class2_amount = 6205
    class4_amount = 8425
    class4_higher_amount = 46351

    no_nic_model = NicModel(0)
    class2_model = NicModel(class2_amount)
    class4_model = NicModel(class4_amount)
    class4_higher_rate_model = NicModel(class4_higher_amount)
    
    def test_get_nic_class(self):
        """
        Test that get_nic_class() returns the correct value
        """
        self.assertEquals(self.no_nic_model.get_nic_class(), 0)
        self.assertEquals(self.class2_model.get_nic_class(), 2)
        self.assertEquals(self.class4_model.get_nic_class(), 4)
        
    def test_get_nic_amount_when_0(self):
        """
        Test that get_nic_amount() returns 0 when no nic class set
        """
        no_nic_amount = self.no_nic_model.get_nic_amount()
        self.assertEquals(no_nic_amount, 0)

    @patch.object(class2_model, 'get_class2_amount') 
    def test_get_nic_amount_class2(self, mock):
        """
        Test that get_nic_amount() calls get_class2_amounth() 
        and returns the correct value for class 2
        """ 
        nic_amount = self.class2_model.get_nic_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(nic_amount, None)
        self.assertEquals(nic_amount, self.class2_model.get_class2_amount())

    """
    Test that get_nic_amount() calls get_class4_amount() 
    for nic class 4
    """
    @patch.object(class4_model, 'get_class4_amount')    
    def test_get_nic_amount_class4(self, mock):
        nic_amount = self.class4_model.get_nic_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(nic_amount, None)
    
    @patch.object(class4_higher_rate_model, 'get_class4_higher_amount') 
    def test_get_class4_amount(self, mock):
        """
        Test that get_class4_amount() performs the correct calculation
        when profit is below the higher threshold
        """
        nic_amount = self.class4_model.get_class4_amount()
        expected_amount = (self.class4_amount - self.class4_model.class4_threshold) * 0.09
        self.assertFalse(mock.called)
        self.assertNotEquals(nic_amount, None)
        self.assertEquals(nic_amount, expected_amount)
    
    @patch.object(class4_higher_rate_model, 'get_class4_higher_amount') 
    def test_get_class4_amount_for_higher_rate(self, mock):
        """
        Test that get_class4_amount() calls get_class4_higher_amount()
        when profit is above the higher threshold
        """
        nic_amount = self.class4_higher_rate_model.get_class4_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(nic_amount, None)
        self.assertEquals(nic_amount, self.class4_higher_rate_model.get_class4_higher_amount())
    
    def test_get_class4_higher_amount(self):
        """
        Test algorithm for get_class4_higher_amount()
        """
        nic_amount = self.class4_higher_rate_model.get_class4_higher_amount()
        self.assertEquals(nic_amount, 3413.36)        