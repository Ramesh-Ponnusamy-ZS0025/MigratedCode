
import unittest
from your_module import count_late_payments  # replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # assume this customer has late payments in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 2)  # assume there are 2 late payments for this customer

    def test_customer_without_late_payments(self):
        customer_id = 2  # assume this customer has no late payments in the database
        late_pay_count = count_late_payments(customer_id)
        self.assertEqual(late_pay_count, 0)

    def test_customer_id_not_found(self):
        customer_id = 999  # assume this customer does not exist in the database
        with self.assertRaises(psycopg2.Error):
            count_late_payments(customer_id)

if __name__ == '__main__':
    unittest.main()
