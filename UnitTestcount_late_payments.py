
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_late_payments_found(self):
        customer_id = 1  # Replace with a valid customer ID
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # Replace with the expected count

    def test_no_late_payments_found(self):
        customer_id = 2  # Replace with a customer ID with no late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # Replace with an invalid customer ID
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

if __name__ == '__main__':
    unittest.main()
