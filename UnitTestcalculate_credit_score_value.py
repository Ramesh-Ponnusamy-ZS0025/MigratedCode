
import unittest
from your_module import calculate_credit_score_value

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_high_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 12000
        credit_card_balance = 0
        late_pay_count = 0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), 850)

    def test_low_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 5000
        late_pay_count = 5
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), 300)

    def test_mid_credit_score(self):
        total_loan_amount = 5000
        total_repayment = 7500
        credit_card_balance = 2000
        late_pay_count = 2
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), 540.0)

if __name__ == '__main__':
    unittest.main()
