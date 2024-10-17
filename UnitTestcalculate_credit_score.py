
import unittest
from calculate_credit_score import calculate_credit_score

class TestCalculateCreditScore(unittest.TestCase):
    def test_calculate_credit_score(self):
        customer_id = 1  # Replace with a valid customer ID
        credit_score = calculate_credit_info(customer_id)
        self.assertEquals(credit_score, 750)  # Replace with an expected credit score value

    def test_calculate_credit_score_low_score(self):
        customer_id = 2  # Replace with a valid customer ID
        credit_score = calculate_credit_info(customer_id)
        self.assertEquals(credit_score, 350)  # Replace with an expected low credit score value

    def test_calculate_credit_score_error(self):
        customer_id = None  # Pass an invalid customer ID to test error handling
        with self.assertRaises(psycopg2.Error):
            calculate_credit_info(customer_id)

if __name__ == '__main__':
    unittest.main()
