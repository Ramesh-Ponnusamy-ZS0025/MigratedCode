
import unittest
from your_module import calculate_credit_score

class TestCalculateCreditScore(unittest.TestCase):
    def test_credit_score_average(self):
        customer_id = 1  # assume this customer has a mix of loans, credit cards, and payments
        score = calculate_credit_score(customer_id)
        self.assertEqual(score, 600)  # assuming an average credit score for this customer

    def test_credit_score_good(self):
        customer_id = 2  # assume this customer has no late payments and good credit habits
        score = calculate_credit_score(customer_id)
        self.assertEqual(score, 800)  # assuming a good credit score for this customer

    def test_credit_score_bad(self):
        customer_id = 3  # assume this customer has multiple late payments and high credit card balances
        score = calculate_credit_score(customer_id)
        self.assertEqual(score, 400)  # assuming a bad credit score for this customer

if __name__ == '__main__':
    unittest.main()
