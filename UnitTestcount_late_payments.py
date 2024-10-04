
import unittest
from your_module import count_late_payments  # Replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # Replace with a customer ID that has late payments in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 2)  # Replace with the expected count of late payments for this customer

    def test_customer_without_late_payments(self):
        customer_id = 2  # Replace with a customer ID that has no late payments in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)

    def test_nonexistent_customer(self):
        customer_id = 999  # Replace with a customer ID that does not exist in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)

if __name__ == '__main__':
    unittest.main()
