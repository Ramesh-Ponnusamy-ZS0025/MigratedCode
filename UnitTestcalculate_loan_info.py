
import unittest
from your_module import calculate_loan_info  # replace 'your_module' with the actual module name

class TestCalculateLoanInfo(unittest.TestCase):
    def test_calculate_loan_info_customer Exists(self):
        customer_id = 1  # assuming customer with id 1 exists in the database
        loan_amount, repayment_amount, outstanding_balance = calculate_loan_info(customer_id)
        self.assertEquals((loan_amount, repayment_amount, outstanding_balance), (1000.0, 500.0, 500.0))  # adjust the expected values accordingly

    def test_calculate_loan_info_customerDoesNotExist(self):
        customer_id = 100  # assuming customer with id 100 does not exist in the database
        loan_amount, repayment_amount, outstanding_balance = calculate_loan_info(customer_id)
        self.assertEquals((loan_amount, repayment_amount, outstanding_balance), (0.0, 0.0, 0.0))

    def test_calculate_loan_info_databaseError(self):
        customer_id = 1  # assuming customer with id 1 exists in the database
        with self.assertRaises(psycopg2.Error):
            calculate_loan_info(customer_id)  # simulate a database error

if __name__ == '__main__':
    unittest.main()
