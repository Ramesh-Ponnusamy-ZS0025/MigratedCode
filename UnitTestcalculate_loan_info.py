
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_customer_id_1(self):
        result = calculate_loan_info(1)
        self.assertEqual(result["total_loan_amount"], 100.0)  # assuming this is the expected value

    def test_customer_id_2(self):
        result = calculate_loan_info(2)
        self.assertEqual(result["total_repayment"], 50.0)  # assuming this is the expected value

    def test_customer_id_3(self):
        result = calculate_loan_info(3)
        self.assertEqual(result["outstanding_loan_balance"], 200.0)  # assuming this is the expected value

    def test_invalid_customer_id(self):
        result = calculate_loan_info(999)  # assuming this customer ID does not exist
        self.assertIsNone(result)  # or you can assert a specific error message

if __name__ == "__main__":
    unittest.main()
