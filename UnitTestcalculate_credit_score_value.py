
import unittest
from your_module import calculate_credit_score_value

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_high_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 10000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 850
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_medium_credit_score(self):
        total_loan_amount = 5000
        total_repayment = 4000
        credit_card_balance = 2000
        late_pay_count = 1
        expected_credit_score = 550
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_low_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 0
        credit_card_balance = 10000
        late_pay_count = 5
        expected_credit_score = 300
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
