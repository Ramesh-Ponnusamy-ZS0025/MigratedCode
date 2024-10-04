
import unittest
from your_module import calculate_credit_score_value  # replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_with_loan_and_credit_card(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 2000
        late_pay_count = 0
        expected_credit_score = 740
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_without_loan(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 5000
        late_pay_count = 2
        expected_credit_score = 550
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_high_late_pay_count(self):
        total_loan_amount = 5000
        total_repayment = 4000
        credit_card_balance = 0
        late_pay_count = 5
        expected_credit_score = 350
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
