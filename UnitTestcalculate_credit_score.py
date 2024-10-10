
import unittest
from your_module import calculate_credit_score

class TestCalculateCreditScore(unittest.TestCase):
    def test_calculate_credit_score(self):
        customer_id = 1
        expected_credit_score = 700
        actual_credit_score = calculate_credit_score(customer_id)
        self.assertEqual(actual_credit_score, expected_credit_score)

    def test_low_credit_score_alert(self):
        customer_id = 2
        expected_credit_score = 400
        actual_credit_score = calculate_credit_score(customer_id)
        self.assertEqual(actual_credit_score, expected_credit_score)

    def test_high_credit_score(self):
        customer_id = 3
        expected_credit_score = 850
        actual_credit_score = calculate_credit_score(customer_id)
        self.assertEqual(actual_credit_score, expected_credit_score)

if __name__ == '__main__':
    unittest.main()
