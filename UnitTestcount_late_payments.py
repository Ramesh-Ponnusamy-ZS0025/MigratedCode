
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_id_1(self):
        result = count_late_payments(1)
        self.assertEqual(result, 2)  # Assuming there are 2 late payments for customer ID 1

    def test_customer_id_2(self):
        result = count_late_payments(2)
        self.assertEqual(result, 0)  # Assuming there are no late payments for customer ID 2

    def test_invalid_customer_id(self):
        result = count_late_payments(-1)
        self.assertEqual(result, 0)  # Assuming no records found for invalid customer ID

if __name__ == '__main__':
    unittest.main()
