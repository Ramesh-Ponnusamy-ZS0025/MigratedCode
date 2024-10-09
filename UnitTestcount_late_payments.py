
import unittest
from your_module import count_late_payments  # replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_count_late_payments(self):
        # Test with a customer ID that has late payments
        customer_id = 1  # assume customer 1 has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # assume there are 2 late payments for customer 1

    def test_count_late_payments_no_late_payments(self):
        # Test with a customer ID that has no late payments
        customer_id = 2  # assume customer 2 has no late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_count_late_payments_invalid_customer_id(self):
        # Test with an invalid customer ID
        customer_id = -1  # assume this customer ID does not exist
        with self.assertRaises(psycopg2.Error):
            count_late_payments(customer_id)

if __name__ == '__main__':
    unittest.main()
