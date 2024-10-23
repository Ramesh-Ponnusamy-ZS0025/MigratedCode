
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_late_payments_found(self):
        customer_id = 1  # Assuming there are late payments for customer 1
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # Assuming there are 2 late payments for customer 1

    def test_no_late_payments_found(self):
        customer_id = 2  # Assuming there are no late payments for customer 2
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # Assuming this customer ID does not exist
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)  # Should return 0 if customer ID is invalid
