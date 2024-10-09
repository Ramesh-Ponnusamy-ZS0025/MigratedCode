
import unittest
from your_module import calculate_loan_info  # Replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_valid_customer_id(self):
        customer_id = 1  # Replace with a valid customer ID
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(outstanding_loan_balance, 1000.0)  # Replace with the expected value

    def test_calculate_loan_info_invalid_customer_id(self):
        customer_id = -1  # Replace with an invalid customer ID
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(total_loan_amount, 0.0)  # Replace with the expected value

    def test_calculate_loan_info_no_loans(self):
        customer_id = 2  # Replace with a customer ID with no loans
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(total_repayment, 0.0)  # Replace with the expected value

if __name__ == '__main__':
    unittest.main()
