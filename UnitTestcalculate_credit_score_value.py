
import unittest
from your_module import calculate_credit_score_value  # replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_with_positive_loan_amount(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 2000
        late_pay_count = 2
        expected_credit_score = 660.0  # calculated manually based on the formula
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_zero_loan_amount(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 2000
        late_pay_count = 2
        expected_credit_score = 550.0  # calculated manually based on the formula
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_high_late_pay_count(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 2000
        late_pay_count = 10
        expected_credit_score = 300.0  # calculated manually based on the formula
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
