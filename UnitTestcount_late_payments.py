
import unittest
from your_module import count_late_payments  # replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_count_late_payments_customer_id_1(self):
        customer_id = 1
        expected_count = 2  # assuming there are 2 late payments for customer 1
        self.assertEqual(count_late_payments(customer_id), expected_count)

    def test_count_late_payments_customer_id_2(self):
        customer_id = 2
        expected_count = 0  # assuming there are no late payments for customer 2
        self.assertEqual(count_late_payments(customer_id), expected_count)

    def test_count_late_payments_invalid_customer_id(self):
        customer_id = -1
        expected_count = 0  # assuming no customer with id -1 exists
        self.assertEqual(count_late_payments(customer_id), expected_count)

if __name__ == '__main__':
    unittest.main()
