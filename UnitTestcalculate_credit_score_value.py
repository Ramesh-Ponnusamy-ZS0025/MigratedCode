
import unittest
from your_module import calculate_credit_score_value  # Import the function from your module

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_perfect_credit(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 850
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_good_credit(self):
        total_loan_amount = 10000
        total_repayment = 12000
        credit_card_balance = 5000
        late_pay_count = 1
        expected_credit_score = 740.0  # calculated manually
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_poor_credit(self):
        total_loan_amount = 50000
        total_repayment = 30000
        credit_card_balance = 15000
        late_pay_count = 3
        expected_credit_score = 380.0  # calculated manually
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
