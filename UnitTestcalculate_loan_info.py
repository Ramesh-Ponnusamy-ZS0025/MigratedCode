
import unittest
from your_module import calculate_loan_info  # Replace 'your_module' with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_existing_customer(self):
        customer_id = 1  # Replace with a known customer ID in your database
        loan_amount, repayment, outstanding_balance = calculate_loan_info(customer_id)
        self.assertEqual(outstanding_balance, 500.00)  # Replace with the expected value for this customer

    def test_non_existing_customer(self):
        customer_id = 9999  # Replace with a non-existing customer ID in your database
        loan_amount, repayment, outstanding_balance = calculate_loan_info(customer_id)
        self.assertEqual(outstanding_balance, 0.00)

    def test_zero_loan_amount(self):
        customer_id = 2  # Replace with a customer ID with zero loan amount
        loan_amount, repayment, outstanding_balance = calculate_loan_info(customer_id)
        self.assertEqual(loan_amount, 0.00)

if __name__ == '__main__':
    unittest.main()
