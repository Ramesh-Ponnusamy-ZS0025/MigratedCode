
import unittest
from your_module import calculate_loan_info  # Replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_with_loans(self):
        result = calculate_loan_info(1)  # Assuming customer_id 1 has loans
        self.assertEquals(result['total_loan_amount'], 1000.00)

    def test_customer_without_loans(self):
        result = calculate_loan_info(2)  # Assuming customer_id 2 has no loans
        self.assertEquals(result['total_loan_amount'], 0.00)

    def test_invalid_customer_id(self):
        result = calculate_loan_info(-1)  # Assuming customer_id -1 does not exist
        self.assertEquals(result['total_loan_amount'], 0.00)

if __name__ == '__main__':
    unittest.main()
