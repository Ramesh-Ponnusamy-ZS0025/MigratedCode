
import unittest
from your_module import calculate_credit_score_value  # Replace 'your_module' with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_calculate_credit_score_value_all_positive(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 700
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_calculate_credit_score_value_late_payments(self):
        total_loan_amount = 5000
        total_repayment = 4000
        credit_card_balance = 0
        late_pay_count = 2
        expected_credit_score = 550
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_calculate_credit_score_value_high_credit_card_balance(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 9000
        late_pay_count = 0
        expected_credit_score = 300
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_calculate_credit_score_value_no_loan(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 700
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
