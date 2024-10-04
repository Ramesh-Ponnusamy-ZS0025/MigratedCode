
import unittest
from your_module import calculate_credit_score

class TestCalculateCreditScore(unittest.TestCase):
    def test_calculate_credit_score(self):
        # Test with a valid customer ID
        customer_id = 123
        credit_score = calculate_credit_score(customer_id)
        self.assertEquals(credit_score, 600)  # Replace with expected credit score

    def test_invalid_customer_id(self):
        # Test with an invalid customer ID
        customer_id = -1
        with self.assertRaises(Exception):
            calculate_credit_score(customer_id)

    def test_no_credit_score(self):
        # Test with a customer ID that doesn't have a credit score
        customer_id = 456
        with self.assertRaises(Exception):
            calculate_credit_score(customer_id)

if __name__ == '__main__':
    unittest.main()
