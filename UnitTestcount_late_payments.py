
import unittest
from your_module import count_late_payments  # replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_with_late_payments(self):
        customer_id = 1  # assume customer 1 has late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 2)  # assuming customer 1 has 2 late payments

    def test_customer_without_late_payments(self):
        customer_id = 2  # assume customer 2 has no late payments
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_non_existent_customer(self):
        customer_id = 999  # assume customer 999 does not exist
        late_pay_count = count_late_payments(customer_id)
        self.assertEquals(late_pay_count, 0)

if __name__ == '__main__':
    unittest.main()
