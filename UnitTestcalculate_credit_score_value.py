
import unittest
from your_module import calculate_credit_score_value  # Replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_with_positive_loan_amount(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 2000
        late_pay_count = 0
        expected_credit_score = 740.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_zero_loan_amount(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 800
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_high_credit_card_balance(self):
        total_loan_amount = 5000
        total_repayment = 2000
        credit_card_balance = 9000
        late_pay_count = 1
        expected_credit_score = 520.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
