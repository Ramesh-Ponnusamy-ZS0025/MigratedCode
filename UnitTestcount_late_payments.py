
import unittest
from your_module import count_late_payments

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 123
        result = count_late_payments(customer_id)
        self.assertEqual(result, 2)  # assuming customer 123 has 2 late payments

    def test_customer_with_no_late_payments(self):
        customer_id = 456
        result = count_late_payments(customer_id)
        self.assertEqual(result, 0)  # assuming customer 456 has no late payments

    def test_invalid_customer_id(self):
        customer_id = -1
        with self.assertRaises Регexels as e:
            count_late_payments(customer_id)
        self.assertIn("Invalid customer ID", str(e))

if __name__ == '__main__':
    unittest.main()
