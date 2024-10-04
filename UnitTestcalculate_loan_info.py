
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_valid_customer_id(self):
        customer_id = 1  # assume this customer ID has loan records
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(outstanding_loan_balance, 1000.0)  # replace with expected value

    def test_invalid_customer_id(self):
        customer_id = 999  # assume this customer ID has no loan records
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(total_loan_amount, 0.0)  # expect zero values for non-existent customer

    def test_multiple_loan_records(self):
        customer_id = 2  # assume this customer ID has multiple loan records
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertEquals(total_repayment, 500.0)  # replace with expected value

if __name__ == '__main__':
    unittest.main()
