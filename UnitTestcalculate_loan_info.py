
import unittest
from your_module import calculate_loan_info  # Replace 'your_module' with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_valid_customer_id(self):
        result = calculate_loan_info(1)
        self.assertNotEqual(result, None)
        self.assertEqual(result["total_loan_amount"], 100.0)  # Replace with the expected value

    def test_calculate_loan_info_invalid_customer_id(self):
        result = calculate_loan_info(999)
        self.assertIsNone(result)

    def test_calculate_loan_info_empty_loan_data(self):
        # Assume there's no loan data for customer_id = 2
        result = calculate_loan_info(2)
        self.assertIsNotNone(result)
        self.assertEqual(result["total_loan_amount"], 0.0)

if __name__ == '__main__':
    unittest.main()
