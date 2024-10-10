
import unittest
from your_module import calculate_credit_score  # Replace with the actual module name

class TestCalculateCreditScore(unittest.TestCase):
    def test_credit_score_update(self):
        customer_id = 123
        expected_credit_score = 600
        actual_credit_score = calculate_credit_score(customer_id)
        self.assertEquals(actual_credit_score, expected_credit_score)

    def test_credit_score_alert(self):
        customer_id = 456
        calculate_credit_score(customer_id)
        # Check if a new record is inserted into the credit_score_alerts table
        conn = engine.connect()
        result = conn.execute("SELECT * FROM credit_score_alerts WHERE customer_id = %s", (customer_id,))
        self.assertIsNotNone(result.fetchone())
        conn.close()

    def test_connection_close(self):
        customer_id = 789
        calculate_credit_score(customer_id)
        # Check if the connection is closed
        self.assertRaises(psycopg2.Error, engine.connect().close)

if __name__ == '__main__':
    unittest.main()
