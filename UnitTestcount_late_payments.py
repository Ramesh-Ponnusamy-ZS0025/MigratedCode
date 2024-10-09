
import unittest
from your_module import count_late_payments  # Replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # Replace with a customer ID that has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # Replace with the expected count

    def test_customer_without_late_payments(self):
        customer_id = 2  # Replace with a customer ID that doesn't have late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # Invalid customer ID
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, None)

if __name__ == '__main__':
    unittest.main()
