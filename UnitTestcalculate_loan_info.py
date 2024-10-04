
import unittest
from your_module import get_loan_summary  # replace with the actual module name

class TestGetLoanSummary(unittest.TestCase):
    def test_get_loan_summary_customer_1(self):
        result = get_loan_summary(1)
        self.assertEqual(result['total_loan_amount'], 1000.0)  # expected value for customer 1

    def test_get_loan_summary_customer_2(self):
        result = get_loan_summary(2)
        self.assertEqual(result['total_repayment'], 500.0)  # expected value for customer 2

    def test_get_loan_summary_customer_nonexistent(self):
        result = get_loan_summary(9999)  # customer doesn't exist
        self.assertEqual(result['outstanding_loan_balance'], 0.0)  # expected default value

if __name__ == '__main__':
    unittest.main()
