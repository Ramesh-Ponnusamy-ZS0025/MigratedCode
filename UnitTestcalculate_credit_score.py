
import unittest
from your_module import calculate_credit_score

class TestCalculateCreditScore(unittest.TestCase):
    def test_calculate_credit_score(self):
        customer_id = 1
        expected_credit_score = 700
        actual_credit_score = calculate_credit_score(customer_id)
        self.assertEqual(actual_credit_score, expected_credit_score)

    def test_update_customer_credit_score(self):
        customer_id = 2
        calculate_credit_score(customer_id)
        with engine.connect() as connection:
            result = connection.execute("SELECT credit_score FROM customers WHERE id = :customer_id", {"customer_id": customer_id})
            actual_credit_score = result.fetchone()[0]
            self.assertEqual(actual_credit_score, 650)  # assume the calculated credit score is 650

    def test_log_low_credit_score_alert(self):
        customer_id = 3
        calculate_credit_score(customer_id)
        with engine.connect() as connection:
            result = connection.execute("SELECT * FROM credit_score_alerts WHERE customer_id = :customer_id", {"customer_id": customer_id})
            self.assertIsNotNone(result.fetchone())

if __name__ == '__main__':
    unittest.main()
