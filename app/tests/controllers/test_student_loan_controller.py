from unittest import TestCase, mock
from unittest.mock import patch
from app.src.commons import Commons as commons
from app.src.controllers.student_loan_controller import StudentLoanController
class TestStudentLoanController(TestCase):  
    """
    Test Class for StudentLoanController
    """
    def test_calc_repayments_returns_0(self):
        """
        Test that calc_repayments() returns 0 for both cases
        1) no sutdent loan plan is set
        2) salary is less than the threshold
        """
        zero_student_loan_ctrl = StudentLoanController(10000, 0)
        no_plan_amount = zero_student_loan_ctrl.calc_repayments()

        zero_student_loan_ctrl.plan = 1
        no_salary_amount = zero_student_loan_ctrl.calc_repayments()

        self.assertIsNotNone(no_plan_amount)
        self.assertIsNotNone(no_salary_amount)

        self.assertEquals(no_plan_amount, 0)
        self.assertEquals(no_salary_amount, 0)

    def test_calc_repayments_throws_exception(self):
        """
        Test that calc_repayments() handles exceptions
        """
        error_student_loan_ctrl = StudentLoanController(10000, None)
        self.assertRaises(Exception, error_student_loan_ctrl.calc_repayments())




        