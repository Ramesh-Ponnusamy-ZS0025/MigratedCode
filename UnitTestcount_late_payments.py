
import unittest
from your_module import count_late_payments  # replace 'your_module' with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_count_late_payments_customer_id_1(self):
        late_pay_count = count_late_payments(1)
        self.assertEquals(late_pay_count, 2)  # assuming there are 2 late payments for customer_id 1

    def test_count_late_payments_customer_id_2(self):
        late_pay_count = count_late_payments(2)
        self.assertEquals(late_pay_count, 0)  # assuming there are no late payments for customer_id 2

    def test_count_late_payments_invalid_customer_id(self):
        late_pay_count = count_late_payments(-1)
        self.assertEquals(late_pay_count, 0)  # assuming no customer_id -1 exists

if __name__ == '__main__':
    unittest.main()
