
import unittest

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_high_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 10000
        credit_card_balance = 0
        late_pay_count = 0
        result = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(result, 850)

    def test_low_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 0
        credit_card_balance = 10000
        late_pay_count = 5
        result = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(result, 300)

    def test_medium_credit_score(self):
        total_loan_amount = 5000
        total_repayment = 4000
        credit_card_balance = 2000
        late_pay_count = 1
        result = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(result, 642.22)  # expected value calculated manually

if __name__ == '__main__':
    unittest.main()
