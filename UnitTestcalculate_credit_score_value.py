
import unittest
from your_module import calculate_credit_score_value  # Replace 'your_module' with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_high_credit_score(self):
        total_loan_amount = 10000
        total_repayment = 10000
        credit_card_balance = 0
        late_pay_count = 0
        credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(credit_score, 850)

    def test_low_credit_score(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 10000
        late_pay_count = 5
        credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(credit_score, 300)

    def test_average_credit_score(self):
        total_loan_amount = 5000
        total_repayment = 4000
        credit_card_balance = 2000
        late_pay_count = 1
        credit_score = calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(credit_score, 563.33)  # Note: This value may vary depending on the actual calculation

if __name__ == '__main__':
    unittest.main()
