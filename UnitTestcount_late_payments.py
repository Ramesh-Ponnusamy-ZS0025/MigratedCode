
import unittest
from your_module import count_late_payments  # replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_late_payments_found(self):
        result = count_late_payments(1)  # assuming customer_id 1 has late payments
        self.assertEquals(result, 2)  # assuming there are 2 late payments for customer 1

    def test_no_late_payments(self):
        result = count_late_payments(2)  # assuming customer_id 2 has no late payments
        self.assertEquals(result, 0)

    def test_invalid_customer_id(self):
        with self.assertRaises(psycopg2.Error):
            count_late_payments(-1)  # assuming customer_id -1 does not exist

if __name__ == '__main__':
    unittest.main()
