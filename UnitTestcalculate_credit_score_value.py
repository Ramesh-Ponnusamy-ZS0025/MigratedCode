
import unittest

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_with_positive_loan_amount(self):
        total_loan_amount = 1000
        total_repayment = 500
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 400
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_zero_loan_amount(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 700
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_negative_credit_card_balance(self):
        total_loan_amount = 1000
        total_repayment = 500
        credit_card_balance = -100
        late_pay_count = 0
        expected_credit_score = 700
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_high_late_pay_count(self):
        total_loan_amount = 1000
        total_repayment = 500
        credit_card_balance = 0
        late_pay_count = 5
        expected_credit_score = 300
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
