
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # assume this customer has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # assume there are 2 late payments for this customer

    def test_customer_with_no_late_payments(self):
        customer_id = 2  # assume this customer has no late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # assume this customer ID does not exist
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)  # assume no late payments for non-existent customer

if __name__ == '__main__':
    unittest.main()
