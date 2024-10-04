
import unittest
from your_module import calculate_loan_info  # Replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_customer_id_1(self):
        result = calculate_loan_info(1)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 1000.0)  # Assuming total_loan_amount for customer_id 1 is 1000.0

    def test_calculate_loan_info_customer_id_nonexistent(self):
        result = calculate_loan_info(100)
        self.assertIsNone(result)

    def test_calculate_loan_info customer_id_none(self):
        with self.assertRaises(TypeError):
            calculate_loan_info(None)

if __name__ == '__main__':
    unittest.main()
