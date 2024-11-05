
import unittest
from your_module import calculate_loan_info  # replace 'your_module' with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_id_1(self):
        result = calculate_loan_info(1)
        self.assertEqual(result, (1000.0, 500.0, 500.0))  # assumes the expected result for customer_id 1

    def test_customer_id_2(self):
        result = calculate_loan_info(2)
        self.assertEqual(result, (2000.0, 1000.0, 1000.0))  # assumes the expected result for customer_id 2

    def test_non_existent_customer_id(self):
        result = calculate_loan_info(999)
        self.assertEqual(result, (0.0, 0.0, 0.0))  # assumes the expected result for a non-existent customer_id

if __name__ == '__main__':
    unittest.main()
