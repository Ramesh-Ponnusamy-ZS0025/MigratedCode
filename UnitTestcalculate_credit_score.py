
import unittest
from your_module import calculate_credit_score  # Replace with the actual module name

class TestCalculateCreditScore(unittest.TestCase):
    def test_calculate_credit_score(self):
        # Test with a valid customer ID
        customer_id = 123
        calculate_credit_score(customer_id)
        self.assertEqual(get_customer_credit_score(customer_id), 700)  # Replace with the expected credit score

    def test_calculate_credit_score_low_score(self):
        # Test with a customer ID that should trigger a low score alert
        customer_id = 456
        calculate_credit_score(customer_id)
        self.assertEqual(get_customer_credit_score(customer_id), 300)  # Replace with the expected credit score

    def test_calculate_credit_score_nonexistent_customer(self):
        # Test with a non-existent customer ID
        customer_id = 789
        with self.assertRaises(psycopg2.Error):
            calculate_credit_score(customer_id)

def get_customer_credit_score(customer_id):
    # Helper function to retrieve the customer's credit score
    connection = engine.connect()
    query = text("SELECT credit_score FROM customers WHERE id = :customer_id")
    result = connection.execute(query, {'customer_id': customer_id})
    credit_score = result.fetchone()[0]
    connection.close()
    return credit_score

if __name__ == '__main__':
    unittest.main()
