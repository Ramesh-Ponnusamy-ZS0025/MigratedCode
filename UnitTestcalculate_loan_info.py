
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_with_loans(self):
        customer_id = 1  # assume this customer has loans in the database
        result = calculate_loan_info(customer_id)
        self.assertEquals(result['total_loan_amount'], 1000.0)  # replace with expected value

    def test_customer_without_loans(self):
        customer_id = 2  # assume this customer has no loans in the database
        result = calculate_loan_info(customer_id)
        self.assertEquals(result['total_loan_amount'], 0.0)

    def test_invalid_customer_id(self):
        customer_id = -1  # assume this customer ID is invalid
        with self.assertRaises(Exception):  # expect an exception when querying the database
            calculate_loan_info(customer_id)

if __name__ == '__main__':
    unittest.main()
