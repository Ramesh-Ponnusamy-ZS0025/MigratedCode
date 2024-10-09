
import unittest
from your_module import calculate_credit_score_value  # replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_good_credit(self):
        total_loan_amount = 10000
        total_repayment = 10000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 850
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_average_credit(self):
        total_loan_amount = 5000
        total_repayment = 4000
        credit_card_balance = 2000
        late_pay_count = 1
        expected_credit_score = 650
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_poor_credit(self):
        total_loan_amount = 20000
        total_repayment = 5000
        credit_card_balance = 8000
        late_pay_count = 3
        expected_credit_score = 350
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
