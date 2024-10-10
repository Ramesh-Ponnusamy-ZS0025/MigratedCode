
import unittest
from your_module import calculate_loan_info  # replace with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info-existing_customer(self):
        customer_id = 1  # assume this customer exists in the database
        total_loan_amount, total_repayment, outstanding_loan_balance = calculate_loan_info(customer_id)
        self.assertIsNotNone(total_loan_amount)
        self.assertIsNotNone(total_repayment)
        self.assertIsNotNone(outstanding_loan_balance)
        self.assertEquals(total_loan_amount, 100.0)  # replace with the expected value

    def test_calculate_loan_info_non_existing_customer(self):
        customer_id = 999  # assume this customer does not exist in the database
        result = calculate_loan_info(customer_id)
        self.assertIsNone(result)

    def test_calculate_loan_info_database_error(self):
        customer_id = 1  # assume this customer exists in the database
        # simulate a database error by temporarily altering the engine URL
        original_engine_url = engine.url
        engine.url = " postgresql://wronguser:wrongpass@wronghost:5432/wrongdb"
        result = calculate_loan_info(customer_id)
        self.assertIsNone(result)
        engine.url = original_engine_url

if __name__ == '__main__':
    unittest.main()
