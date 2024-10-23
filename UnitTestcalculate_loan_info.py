
import unittest
from your_module import calculate_loan_info  # Replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_with_loans(self):
        customer_id = 1  # assume this customer has loans in the database
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(outstanding_loan_balance, 500.00)  # example value, adjust according to your data

    def test_customer_without_loans(self):
        customer_id = 2  # assume this customer has no loans in the database
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(total_loan_amount, 0.00)  # example value, adjust according to your data

    def test_invalid_customer_id(self):
        customer_id = -1  # invalid customer ID
        with self.assertRaises(Exception):
            calculate_loan_info(customer_id)

if __name__ == '__main__':
    unittest.main()
