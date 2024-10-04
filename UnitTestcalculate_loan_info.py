
import unittest
from your_module import calculate_loan_info  # Replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_with_loans(self):
        customer_id = 1  # assume this customer has loans in the database
        loan_amount, repayment, outstanding_balance = calculate_loan_info(customer_id)
        self.assertEqual(loan_amount, 1000.00)  # replace with expected value

    def test_customer_without_loans(self):
        customer_id = 2  # assume this customer has no loans in the database
        loan_amount, repayment, outstanding_balance = calculate_loan_info(customer_id)
        self.assertEqual(outstanding_balance, 0.00)  # replace with expected value

    def test_invalid_customer_id(self):
        customer_id = -1  # assume this customer does not exist
        with self.assertRaises(Exception):
            calculate_loan_info(customer_id)

if __name__ == '__main__':
    unittest.main()
