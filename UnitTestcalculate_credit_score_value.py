
import unittest
from your_module import calculate_credit_score_value  # replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_high_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 10000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 850
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_low_credit_score(self):
        total_loan_amount = 5000
        total_repayment = 2000
        credit_card_balance = 5000
        late_pay_count = 2
        expected_credit_score = 300
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_medium_credit_score(self):
        total_loan_amount = 8000
        total_repayment = 6000
        credit_card_balance = 2000
        late_pay_count = 1
        expected_credit_score = 620
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
