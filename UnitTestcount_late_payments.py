
import unittest
from your_module import get_late_pay_count  # Replace with the actual module name

class TestGetLatePayCount(unittest.TestCase):
    def test_get_late_pay_count_zero(self):
        # Assume there are no late payments for customer_id=1
        result = get_late_pay_count(1)
        self.assertEquals(result, 0)

    def test_get_late_pay_count_nonzero(self):
        # Assume there are 2 late payments for customer_id=2
        result = get_late_pay_count(2)
        self.assertEquals(result, 2)

    def test_get_late_pay_count_invalid_customer_id(self):
        # Assume customer_id=99 does not exist in the database
        result = get_late_pay_count(99)
        self.assertEquals(result, 0)

if __name__ == '__main__':
    unittest.main()
