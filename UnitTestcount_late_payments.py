
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # Assume this customer has late payments
        count = count_late_payments(customer_id)
        self.assertEqual(count, 2)  # Replace with the expected count

    def test_customer_without_late_payments(self):
        customer_id = 2  # Assume this customer has no late payments
        count = count_late_payments(customer_id)
        self.assertEqual(count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # Assume this customer does not exist
        count = count_late_payments(customer_id)
        self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()
