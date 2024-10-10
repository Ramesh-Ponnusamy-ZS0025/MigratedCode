
import unittest
from your_module import count_late_payments  # replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_count_late_payments_valid_customer_id(self):
        customer_id = 1  # assuming this customer has some late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 2)  # assuming there are 2 late payments for this customer

    def test_count_late_payments_invalid_customer_id(self):
        customer_id = 999  # assuming this customer does not exist
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)  # no late payments for non-existent customer

    def test_count_late_payments_no_late_payments(self):
        customer_id = 2  # assuming this customer has no late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)  # no late payments for this customer

if __name__ == '__main__':
    unittest.main()
