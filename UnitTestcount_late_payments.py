
import unittest
from your_module import count_late_payments  # Replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):

    def test_customer_with_late_payments(self):
        customer_id = 1  # Assuming customer with ID 1 has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 2)  # Replace 2 with the expected count

    def test_customer_without_late_payments(self):
        customer_id = 2  # Assuming customer with ID 2 does not have late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)

    def test_non_existent_customer(self):
        customer_id = 999  # Assuming customer with ID 999 does not exist
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)

if __name__ == '__main__':
    unittest.main()
