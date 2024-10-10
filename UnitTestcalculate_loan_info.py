
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info(self):
        result = calculate_loan_info(1)  # replace with a valid customer ID
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("total_loan_amount", result)
        self.assertIn("total_repayment", result)
        self.assertIn("outstanding_loan_balance", result)
        self.assertEquals(result["total_loan_amount"], 1234.56)  # replace with an expected value

    def test_calculate_loan_info_invalid_customer_id(self):
        with self.assertRaises(psycopg2.Error):
            calculate_loan_info(-1)  # replace with an invalid customer ID

    def test_calculate_loan_info_no_loans(self):
        result = calculate_loan_info(2)  # replace with a customer ID with no loans
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("total_loan_amount", result)
        self.assertIn("total_repayment", result)
        self.assertIn("outstanding_loan_balance", result)
        self.assertEquals(result["total_loan_amount"], 0.0)  # replace with an expected value

if __name__ == "__main__":
    unittest.main()
