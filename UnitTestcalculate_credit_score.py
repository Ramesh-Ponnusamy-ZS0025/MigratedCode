
import unittest
from your_module import calculate_credit_score  # Replace with the actual module name

class TestCalculateCreditScore(unittest.TestCase):
    def test_credit_score_with_loans_and_credit_card(self):
        # Test case: customer has loans and credit card balance
        customer_id = 1
        expected_credit_score = 650
        self.assertEqual(calculate_credit_score(customer_id), expected_credit_score)

    def test_credit_score_with_only_loans(self):
        # Test case: customer has only loans
        customer_id = 2
        expected_credit_score = 700
        self.assertEqual(calculate_credit_score(customer_id), expected_credit_score)

    def test_credit_score_with_only_credit_card(self):
        # Test case: customer has only credit card balance
        customer_id = 3
        expected_credit_score = 550
        self.assertEqual(calculate_credit_score(customer_id), expected_credit_score)

    def test_credit_score_with_no_data(self):
        # Test case: customer has no loans or credit card balance
        customer_id = 4
        expected_credit_score = 400
        self.assertEqual(calculate_credit_score(customer_id), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
