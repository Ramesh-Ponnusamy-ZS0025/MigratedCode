
import unittest
from your_module import calculate_credit_score_value  # Replace with actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_total_loan_amount_greater_than_zero(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 640.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_card_balance_greater_than_zero(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 5000
        late_pay_count = 0
        expected_credit_score = 550.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_late_pay_count_penalty(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 2
        expected_credit_score = 300.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
