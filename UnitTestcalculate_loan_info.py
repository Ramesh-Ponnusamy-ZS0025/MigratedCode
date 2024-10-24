
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_id_123(self):
        result = calculate_loan_info(123)
        self.assertEqual(result, (1000.0, 500.0, 500.0))  # replace with expected values

    def test_customer_id_456(self):
        result = calculate_loan_info(456)
        self.assertEqual(result, (2000.0, 1000.0, 1000.0))  # replace with expected values

    def test_customer_id_nonexistent(self):
        result = calculate_loan_info(789)
        self.assertEqual(result, (0.0, 0.0, 0.0))  # expected default values when no records found

if __name__ == '__main__':
    unittest.main()
