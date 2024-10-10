
import unittest

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_with_positive_loan_amount(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 2000
        late_pay_count = 2
        expected_result = 620.0
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_result)

    def test_credit_score_with_zero_loan_amount(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 0
        expected_result = 700.0
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_result)

    def test_credit_score_with_high_late_pay_count(self):
        total_loan_amount = 5000
        total_repayment = 2500
        credit_card_balance = 1000
        late_pay_count = 6
        expected_result = 300.0
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_result)

if __name__ == '__main__':
    unittest.main()
