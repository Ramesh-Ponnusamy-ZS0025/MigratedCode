
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_valid_customer_id(self):
        result = calculate_loan_info(1)  # assume customer_id 1 exists in the database
        self.assertEquals(result["total_loan_amount"], 1000.0)  # replace with the expected value

    def test_invalid_customer_id(self):
        result = calculate_loan_info(9999)  # assume customer_id 9999 does not exist in the database
        self.assertEquals(result["total_loan_amount"], 0.0)  # expect 0.0 since no records found

    def test_error_handling(self):
        # simulate a database connection error
        with unittest.mock.patch('your_module.engine.connect', side_effect=psycopg2.Error("connection error")):
            with self.assertRaises(psycopg2.Error):
                calculate_loan_info(1)

if __name__ == "__main__":
    unittest.main()
