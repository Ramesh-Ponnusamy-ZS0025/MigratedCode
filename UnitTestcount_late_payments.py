
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_count_late_payments_customer_id_1(self):
        result = count_late_payments(1)
        self.assertEquals(result, 2)  # Assume there are 2 late payments for customer_id 1

    def test_count_late_payments_customer_id_2(self):
        result = count_late_payments(2)
        self.assertEquals(result, 0)  # Assume there are no late payments for customer_id 2

    def test_count_late_payments_invalid_customer_id(self):
        result = count_late_payments(-1)
        self.assertEquals(result, 0)  # Assume no late payments for invalid customer_id

if __name__ == '__main__':
    unittest.main()
