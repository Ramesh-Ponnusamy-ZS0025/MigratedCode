
import unittest
from your_module import calculate_credit_score  # replace with the actual module name

class TestCalculateCreditScore(unittest.TestCase):
    def test_all_good(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 500
        late_pay_count = 0
        result = calculate_credit_score(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(result, 740.0)

    def test_late_payments(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 500
        late_pay_count = 2
        result = calculate_credit_score(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(result, 640.0)

    def test_high_credit_card_balance(self):
        total_loan_amount = 10000
        total_repayment = 8000
        credit_card_balance = 9000
        late_pay_count = 0
        result = calculate_credit_score(total_loan_amount, total_repayment, credit_card_balance, late_pay_count)
        self.assertEquals(result, 540.0)

if __name__ == '__main__':
    unittest.main()
