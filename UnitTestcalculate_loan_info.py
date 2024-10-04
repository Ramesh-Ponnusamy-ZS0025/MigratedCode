
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_with_loans(self):
        result = calculate_loan_info(1)  # assuming customer 1 has loans
        self.assertEqual(result['total_loan_amount'], 1000.0)  # example value

    def test_customer_without_loans(self):
        result = calculate_loan_info(2)  # assuming customer 2 has no loans
        self.assertEqual(result['total_loan_amount'], 0.0)

    def test_invalid_customer_id(self):
        with self.assertRaises(psycopg2.Error):
            calculate_loan_info(-1)  # assuming invalid customer ID

if __name__ == '__main__':
    unittest.main()
