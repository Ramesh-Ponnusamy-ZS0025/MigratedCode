
import unittest
from your_module import count_late_payments  # replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 123  # assume this customer has late payments in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # assume there are 2 late payments for this customer

    def test_customer_without_late_payments(self):
        customer_id = 456  # assume this customer has no late payments in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = -1  # assume this customer ID does not exist in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

if __name__ == '__main__':
    unittest.main()
