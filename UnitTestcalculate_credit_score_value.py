
import unittest
from your_module import calculate_credit_score  # Replace with the actual module name

class TestCalculateCreditScore(unittest.TestCase):
    def test_good_credit(self):
        total_loan_amount = 10000
        total_repayment = 10000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 700
        self.assertEquals(calculate_credit_score(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_bad_credit(self):
        total_loan_amount = 10000
        total_repayment = 5000
        credit_card_balance = 5000
        late_pay_count = 2
        expected_credit_score = 450
        self.assertEquals(calculate_credit_score(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_no_loan(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 700
        self.assertEquals(calculate_credit_score(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
