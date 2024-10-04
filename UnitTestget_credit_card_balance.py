
import unittest
from your_module import get_credit_card_balance  # replace with the actual module name

class TestGetCreditCardBalance(unittest.TestCase):
    def test_customer_with_credit_card_balance(self):
        customer_id = 1  # assume this customer has a credit card balance
        balance = get_credit_card_balance(customer_id)
        self.assertEqual(balance, 123.45)  # replace with the expected balance

    def test_customer_without_credit_card_balance(self):
        customer_id = 2  # assume this customer does not have a credit card balance
        balance = get_credit_card_balance(customer_id)
        self.assertEqual(balance, 0.0)

    def test_invalid_customer_id(self):
        customer_id = -1  # assume this customer does not exist
        balance = get_credit_card_balance(customer_id)
        self.assertEqual(balance, 0.0)

if __name__ == '__main__':
    unittest.main()
