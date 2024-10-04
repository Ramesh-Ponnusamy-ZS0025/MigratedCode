
import unittest
from your_module import get_late_pay_count

class TestGetLatePayCount(unittest.TestCase):

    def test_get_late_pay_count_with_existing_customer(self):
        customer_id = 1  # Replace with an existing customer ID in your database
        late_pay_count = get_late_pay_count(customer_id)
        self.assertEquals(late_pay_count, 2)  # Replace with the expected count for this customer

    def test_get_late_pay_count_with_non_existing_customer(self):
        customer_id = 999  # Replace with a non-existing customer ID in your database
        late_pay_count = get_late_pay_count(customer_id)
        self.assertEquals(late_pay_count, 0)

    def test_get_late_pay_count_with_error(self):
        customer_id = None
        late_pay_count = get_late_pay_count(customer_id)
        self.assertEquals(late_pay_count, None)

if __name__ == '__main__':
    unittest.main()
