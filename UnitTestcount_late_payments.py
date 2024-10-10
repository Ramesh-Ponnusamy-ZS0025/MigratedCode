
import unittest
from your_module import count_late_payments  # replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # assume customer 1 has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 2)  # assume customer 1 has 2 late payments

    def test_customer_without_late_payments(self):
        customer_id = 2  # assume customer 2 doesn't have late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # assume invalid customer id
        with self.assertRaises(Exception):
            count_late_payments(customer_id)

if __name__ == '__main__':
    unittest.main()
