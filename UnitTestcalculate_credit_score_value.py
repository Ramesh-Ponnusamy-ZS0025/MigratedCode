
import unittest
from your_module import calculate_credit_score_value  # replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_good_credit(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 750
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test悪い_credit(self):
        total_loan_amount = 5000
        total_repayment = 1000
        credit_card_balance = 5000
        late_pay_count = 2
        expected_credit_score = 450
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test.credit_card_only(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 2000
        late_pay_count = 0
        expected_credit_score = 550
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
