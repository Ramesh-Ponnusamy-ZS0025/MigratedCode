
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_valid_customer_id(self):
        customer_id = 1  # assume this customer id exists in the database
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(total_loan_amount, 1000.00)  # replace with the expected value

    def test_calculate_loan_info_invalid_customer_id(self):
        customer_id = 9999  # assume this customer id does not exist in the database
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(total_loan_amount, 0.00)  # expect 0.00 for non-existent customer id

    def test_calculate_loan_info_no_loans(self):
        customer_id = 2  # assume this customer id exists but has no loans
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEqual(total_loan_amount, 0.00)  # expect 0.00 for customer with no loans

if __name__ == '__main__':
    unittest.main()
