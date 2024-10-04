
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # Replace with a valid customer ID
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 2)  # Replace with the expected count

    def test_customer_without_late_payments(self):
        customer_id = 2  # Replace with a valid customer ID
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # Replace with an invalid customer ID
        with self.assertRaises(psycopg2.Error):
            count_late_payments(customer_id)

if __name__ == '__main__':
    unittest.main()
