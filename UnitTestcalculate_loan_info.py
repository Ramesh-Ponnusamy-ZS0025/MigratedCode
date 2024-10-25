
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_valid_customer_id(self):
        customer_id = 1  # replace with a valid customer ID
        result = calculate_loan_info(customer_id)
        self.assertIsNotNone(result)
        self.assertEquals(result[0], 1000.00)  # replace with the expected total loan amount

    def test_calculate_loan_info_invalid_customer_id(self):
        customer_id = -1  # replace with an invalid customer ID
        result = calculate_loan_info(customer_id)
        self.assertIsNone(result)

    def test_calculate_loan_info_no_loans_found(self):
        customer_id = 2  # replace with a customer ID with no loans
        result = calculate_loan_info(customer_id)
        self.assertIsNotNone(result)
        self.assertEquals(result[0], 0.00)  # default value when no loans are found

if __name__ == '__main__':
    unittest.main()
