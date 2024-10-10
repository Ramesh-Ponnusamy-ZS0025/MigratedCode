
import unittest
from your_module import calculate_credit_score_value  # Replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_good_credit(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 1000
        late_pay_count = 0
        expected_credit_score = 740  # calculated based on the formulas
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_bad_credit(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 5000
        late_pay_count = 5
        expected_credit_score = 300  # calculated based on the formulas
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test邊界case(self):
        total_loan_amount = 10000
        total_repayment = 10000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 850  # calculated based on the formulas
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
