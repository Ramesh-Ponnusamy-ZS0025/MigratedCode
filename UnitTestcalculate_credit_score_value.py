
import unittest
from your_module import calculate_credit_score_value  # replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_good_credit(self):
        total_loan_amount = 10000
        total_repayment = 9000
        credit_card_balance = 2000
        late_pay_count = 0
        expected_credit_score = 740
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_bad_credit(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 8000
        late_pay_count = 3
        expected_credit_score = 350
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_no_loans(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 700
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
