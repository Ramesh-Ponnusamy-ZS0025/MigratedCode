
import unittest
from your_module import calculate_credit_score_value  # Import the function to be tested

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_credit_score_with_loan(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 0
        late_pay_count = 0
        expected_credit_score = 720.00  # calculated manually
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_no_loan(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 5000
        late_pay_count = 2
        expected_credit_score = 550.00  # calculated manually
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

    def test_credit_score_with_late_payments(self):
        total_loan_amount = 5000
        total_repayment = 4000
        credit_card_balance = 1000
        late_pay_count = 3
        expected_credit_score = 520.00  # calculated manually
        self.assertEqual(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_credit_score)

if __name__ == '__main__':
    unittest.main()
