
import unittest
from your_module import calculate_loan_info  # Import the function from your module

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_customer_exists(self):
        customer_id = 1  # Assuming customer with id 1 exists in the database
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(total_loan_amount, 1000.0)  # Replace with the expected value

    def test_calculate_loan_info_customer_does_not_exist(self):
        customer_id = 999  # Assuming customer with id 999 does not exist in the database
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(total_loan_amount, 0.0)  # Since no records found, loan amount should be 0

if __name__ == '__main__':
    unittest.main()
