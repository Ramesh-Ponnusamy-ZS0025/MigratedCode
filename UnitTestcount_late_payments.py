
import unittest
from your_module import count_late_payments  # Replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_count_late_payments(self):
        # Test with a customer ID that has late payments
        self.assertEquals(count_late_payments(1), 2)

    def test_no_late_payments(self):
        # Test with a customer ID that has no late payments
        self.assertEquals(count_late_payments(2), 0)

    def test_customer_id_not_found(self):
        # Test with a customer ID that does not exist
        self.assertEquals(count_late_payments(999), 0)

if __name__ == '__main__':
    unittest.main()
