
import unittest
from your_module import calculate_credit_score_value  # Replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_calculated_correctly(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 2000
        late_pay_count = 2
        expected_credit_score = 640.0
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_zero_total_loan_amount(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 2000
        late_pay_count = 2
        expected_credit_score = 550.0
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_zero_credit_card_balance(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 0
        late_pay_count = 2
        expected_credit_score = 700.0
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
