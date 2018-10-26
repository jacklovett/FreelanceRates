from unittest import TestCase
from app.src.commons import Commons as commons
class TestCommons(TestCase):
    """
    Test Class for Commons
    """
    def test_diff_or_zero(self):
        """
        Test diff_or_zero calculation
        """
        diff_result = commons.diff_or_zero(2,1)
        zero_result = commons.diff_or_zero(1,2)
        self.assertEquals(diff_result, 1)
        self.assertEquals(zero_result, 0)