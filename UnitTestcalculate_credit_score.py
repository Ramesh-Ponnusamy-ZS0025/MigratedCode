
import unittest
from your_module import calculate_credit_score  # Import the function from your Python file

class TestCalculateCreditScore(unittest.TestCase):
    def test_calculate_credit_score(self):
        # Test with a valid customer ID
        customer_id = 1
        credit_score = calculate_credit_score(customer_id)
        self.assertEqual(credit_score, 600)  # Replace with the expected credit score

    def test_calculate_credit_score_low_score(self):
        # Test with a valid customer ID that should trigger a low score alert
        customer_id = 2
        credit_score = calculate_credit_score(customer_id)
        self.assertEqual(credit_score, 400)  # Replace with the expected credit score

    def test_calculate_credit_score_invalid_customer_id(self):
        # Test with an invalid customer ID
        customer_id = -1
        with self.assertRaises(Exception):  # Replace with the expected exception
            calculate_credit_score(customer_id)

if __name__ == '__main__':
    unittest.main()
