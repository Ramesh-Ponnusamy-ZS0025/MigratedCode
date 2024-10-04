
import unittest
from your_module import get_credit_card_balance  # replace with the actual module name

class TestGetCreditCardBalance(unittest.TestCase):
    def test_existing_customer_with_balance(self):
        customer_id = 1  # assume customer with ID 1 has a credit card balance
        balance = get_credit_card_balance(customer_id)
        self.assertEquals(balance, 100.0)  # replace with the expected balance

    def test_non_existing_customer(self):
        customer_id = 1000  # assume no customer with this ID exists
        balance = get_credit_card_balance(customer_id)
        self.assertEquals(balance, 0.0)  # expect 0 balance for non-existing customer

    def test_customer_with_zero_balance(self):
        customer_id = 2  # assume customer with ID 2 has a credit card balance of 0
        balance = get_credit_card_balance(customer_id)
        self.assertEquals(balance, 0.0)  # expect 0 balance

if __name__ == '__main__':
    unittest.main()
