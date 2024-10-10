
import unittest

class TestCalculateCreditScoreValue(unittest.TestCase):
    def test_perfect_credit(self):
        credit_score = calculate_credit_score_value(0, 0, 0, 0)
        self.assertEquals(credit_score, 850)

    def test_good_credit(self):
        credit_score = calculate_credit_score_value(10000, 5000, 2000, 1)
        self.assertEquals(credit_score, 650)

    def test_bad_credit(self):
        credit_score = calculate_credit_score_value(50000, 0, 10000, 5)
        self.assertEquals(credit_score, 300)

if __name__ == '__main__':
    unittest.main()
