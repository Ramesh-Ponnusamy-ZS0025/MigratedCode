
import unittest
from your_module import count_late_payments  # Replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_late_payments_found(self):
        # Test case where late payments are found for a customer
        customer_id = 1  # assuming this customer has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # assuming there are 2 late payments

    def test_no_late_payments_found(self):
        # Test case where no late payments are found for a customer
        customer_id = 2  # assuming this customer has no late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_invalid_customer_id(self):
        # Test case where an invalid customer ID is provided
        customer_id = -1  # assuming this customer does not exist
        with self.assertRaises(Exception):
            count_late_payments(customer_id)

if __name__ == '__main__':
    unittest.main()
