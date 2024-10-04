
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_valid_customer_id(self):
        result = calculate_loan_info(1)
        self.assertEqual(result['total_loan_amount'], 1000.0)  # assuming this is the expected value

    def test_invalid_customer_id(self):
        result = calculate_loan_info(999)  # assuming this customer ID does not exist
        self.assertEqual(result['outstanding_loan_balance'], 0.0)

    def test_no_loans(self):
        result = calculate_loan_info(2)  # assuming this customer has no loans
        self.assertEqual(result['total_repayment'], 0.0)

if __name__ == '__main__':
    unittest.main()
