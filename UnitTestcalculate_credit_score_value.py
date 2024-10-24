
import unittest
from your_module import calculate_credit_score_value  # replace with the actual module name

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test calcular_credit_score_value_sample1(self):
        total_loan_amount = 1000
        total_repayment = 500
        credit_card_balance = 0
        late_pay_count = 0
        expected_result = 600.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_result)

    def test_calculate_credit_score_value_sample2(self):
        total_loan_amount = 0
        total_repayment = 0
        credit_card_balance = 5000
        late_pay_count = 2
        expected_result = 500.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_result)

    def test_calculate_credit_score_value_sample3(self):
        total_loan_amount = 2000
        total_repayment = 1500
        credit_card_balance = 2000
        late_pay_count = 1
        expected_result = 550.0
        self.assertEquals(calculate_credit_score_value(total_loan_amount, total_repayment, credit_card_balance, late_pay_count), expected_result)

if __name__ == '__main__':
    unittest.main()
