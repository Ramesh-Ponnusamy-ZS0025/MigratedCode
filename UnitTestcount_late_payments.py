
import unittest
from your_module import count_late_payments  # replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_late_payments_found(self):
        customer_id = 1  # assuming this customer has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # assuming 2 late payments for customer 1

    def test_no_late_payments_found(self):
        customer_id = 2  # assuming this customer has no late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_invalid_customer_id(self):
        customer_id = None  # invalid customer ID
        with self.assertRaises(TypeError):
            count_late_payments(customer_id)

if __name__ == '__main__':
    unittest.main()
