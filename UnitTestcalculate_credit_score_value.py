
import unittest
from calculate_credit_score_value import calculate_credit_score_value

class TestCalculateCreditScoreValue(unittest.TestCase):
    def testPositiveTotalLoanAmount(self):
        result = calculate_credit_score_value(10000, 5000, 2000, 2)
        self.assertEquals(result, 650.0)

    def testZeroTotalLoanAmount(self):
        result = calculate_credit_score_value(0, 5000, 2000, 2)
        self.assertEquals(result, 550.0)

    def testHighCreditCardBalance(self):
        result = calculate_credit_score_value(10000, 5000, 8000, 2)
        self.assertEquals(result, 400.0)

    def testLatePayCount(self):
        result = calculate_credit_score_value(10000, 5000, 2000, 4)
        self.assertEquals(result, 500.0)

if __name__ == '__main__':
    unittest.main()
