
import unittest
from your_module import calculate_credit_score_value

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_with_loans(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 720
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_credit_cards(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 5000
        late_pay_count = 0
        expected_credit_score = 650
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_late_pays(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 2
        expected_credit_score = 550
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)
