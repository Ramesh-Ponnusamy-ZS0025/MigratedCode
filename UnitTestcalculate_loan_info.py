
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info(self):
        customer_id = 123
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(total_loan_amount, 1000.0)  # example value

    def test_calculate_loan_info_invalid_customer_id(self):
        customer_id = 999  # invalid customer id
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(total_loan_amount, 0.0)  # expect 0 if no records found

    def test_calculate_loan_info_no_loans(self):
        customer_id = 456  # customer with no loans
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(total_loan_amount, 0.0)  # expect 0 if no loans found
