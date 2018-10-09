from unittest import TestCase, mock
from unittest.mock import patch
from app.src.controllers.nic_controller import NicController
from app.src.constants import Constants as constants

class TestNicController(TestCase):
    """
    Test Class for NicController
    """
     # Class Thresholds
    class2_amount = constants.class2_threshold
    class4_amount = constants.class4_threshold + 1
    class4_higher_amount = constants.class4_higher_threshold + 1

    no_nic_ctrl = NicController(0)
    class2_ctrl = NicController(class2_amount)
    class4_ctrl = NicController(class4_amount)
    class4_higher_rate_ctrl = NicController(class4_higher_amount)
    
    def test_get_nic_class(self):
        """
        Test that get_nic_class() returns the correct value
        """
        self.assertEquals(self.no_nic_ctrl.get_nic_class(), 0)
        self.assertEquals(self.class2_ctrl.get_nic_class(), 2)
        self.assertEquals(self.class4_ctrl.get_nic_class(), 4)
        
    def test_get_nic_amount_when_0(self):
        """
        Test that get_nic_amount() returns 0 when no nic class set
        """
        no_nic_amount = self.no_nic_ctrl.get_nic_amount()
        self.assertEquals(no_nic_amount, 0)

    @patch.object(class2_ctrl, 'get_class2_amount') 
    def test_get_nic_amount_class2(self, mock):
        """
        Test that get_nic_amount() calls get_class2_amounth() 
        and returns the correct value for class 2
        """ 
        nic_amount = self.class2_ctrl.get_nic_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(nic_amount, None)
        self.assertEquals(nic_amount, self.class2_ctrl.get_class2_amount())

    """
    Test that get_nic_amount() calls get_class4_amount() 
    for nic class 4
    """
    @patch.object(class4_ctrl, 'get_class4_amount')    
    def test_get_nic_amount_class4(self, mock):
        nic_amount = self.class4_ctrl.get_nic_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(nic_amount, None)
    
    @patch.object(class4_higher_rate_ctrl, 'get_class4_higher_amount') 
    def test_get_class4_amount(self, mock):
        """
        Test that get_class4_amount() performs the correct calculation
        when profit is below the higher threshold
        """
        nic_amount = self.class4_ctrl.get_class4_amount()
        expected_amount = (self.class4_amount - constants.class4_threshold) * 0.09
        self.assertFalse(mock.called)
        self.assertNotEquals(nic_amount, None)
        self.assertEquals(nic_amount, expected_amount)
    
    @patch.object(class4_higher_rate_ctrl, 'get_class4_higher_amount') 
    def test_get_class4_amount_for_higher_rate(self, mock):
        """
        Test that get_class4_amount() calls get_class4_higher_amount()
        when profit is above the higher threshold
        """
        nic_amount = self.class4_higher_rate_ctrl.get_class4_amount()
        self.assertTrue(mock.called)
        self.assertNotEquals(nic_amount, None)
        self.assertEquals(nic_amount, self.class4_higher_rate_ctrl.get_class4_higher_amount())
    
    def test_get_class4_higher_amount(self):
        """
        Test algorithm for get_class4_higher_amount()
        """
        nic_amount = self.class4_higher_rate_ctrl.get_class4_higher_amount()
        self.assertEquals(nic_amount, 3413.36)    