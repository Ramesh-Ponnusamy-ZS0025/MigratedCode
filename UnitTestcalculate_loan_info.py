
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_valid_customer_id(self):
        result = calculate_loan_info(1)  # assume customer_id 1 has records in the loans table
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[0], 1000.00)  # example total_loan_amount value

    def test_calculate_loan_info_invalid_customer_id(self):
        result = calculate_loan_info(999)  # assume customer_id 999 does not have records in the loans table
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result[0], 0.00)  # default value when no records are found

    def test_calculate_loan_info_none_customer_id(self):
        with self.assertRaises(TypeError):
            calculate_loan_info(None)

if __name__ == '__main__':
    unittest.main()
