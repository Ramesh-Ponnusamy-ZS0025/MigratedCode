
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_customer_id_1(self):
        result = count_late_payments(1)
        self.assertEquals(result, 2)  # assuming there are 2 late payments for customer 1

    def test_customer_id_2(self):
        result = count_late_payments(2)
        self.assertEquals(result, 0)  # assuming there are no late payments for customer 2

    def test_customer_id_non_existent(self):
        result = count_late_payments(999)
        self.assertEquals(result, 0)  # assuming there are no late payments for a non-existent customer

    def test_customer_id_none(self):
        with self.assertRaises(TypeError):
            count_late_payments(None)  # expecting a TypeError when passing None as an argument

if __name__ == '__main__':
    unittest.main()
