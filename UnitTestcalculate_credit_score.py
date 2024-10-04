
import unittest
from your_module import calculate_credit_score, calculate_loan_info, get_credit_card_balance, count_late_payments, calculate_credit_score_value

class TestCreditScoreCalculation(unittest.TestCase):

    def test_calculate_credit_score(self):
        # Assuming customer id 1 has a credit score of 600
        calculate_credit_score(1)
        connection = engine.connect()
        result = connection.execute("SELECT credit_score FROM customers WHERE id = 1").fetchone()
        self.assertEquals(result[0], 600)

    def test_calculate_loan_info(self):
        loan_info = calculate_loan_info(1)
        self.assertEquals(len(loan_info), 3)

    def test_get_credit_card_balance(self):
        balance = get_credit_card_balance(1)
        self.assertIsInstance(balance, float)

    def test_count_late_payments(self):
        count = count_late_payments(1)
        self.assertIsInstance(count, int)

    def test_calculate_credit_score_value(self):
        score = calculate_credit_score_value(1000, 500, 500, 2)
        self.assertIsInstance(score, float)

if __name__ == '__main__':
    unittest.main()
