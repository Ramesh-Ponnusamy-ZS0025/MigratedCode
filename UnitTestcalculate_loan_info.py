
import unittest
from your_module import calculate_loan_info  # Replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_with_loans(self):
        customer_id = 1  # replace with a customer ID that has loans in the database
        result = calculate_loan_info(customer_id)
        self.assertIsNotNone(result)
        total_loan_amount, total_repayment, outstanding_loan_balance = result
        self.assertAlmostEqual(total_loan_amount, 1000.0)  # replace with expected value

    def test_customer_without_loans(self):
        customer_id = 2  # replace with a customer ID that has no loans in the database
        result = calculate_loan_info(customer_id)
        self.assertIsNone(result)

    def test_invalid_customer_id(self):
        customer_id = -1  # invalid customer ID
        result = calculate_loan_info(customer_id)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
