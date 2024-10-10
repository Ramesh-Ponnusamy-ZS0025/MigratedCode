
import unittest
from your_module import get_credit_card_balance

class TestGetCreditCardBalance(unittest.TestCase):
    def test_existing_customer(self):
        customer_id = 1  # replace with a known customer ID
        balance = get_credit_card_balance(customer_id)
        self.assertEquals(balance, 100.00)  # replace with expected balance

    def test_non_existing_customer(self):
        customer_id = 99999  # replace with a non-existing customer ID
        balance = get_credit_card_balance(customer_id)
        self.assertEquals(balance, 0.00)

    def test_multiple_credit_cards(self):
        customer_id = 2  # replace with a customer ID with multiple credit cards
        balance = get_credit_card_balance(customer_id)
        self.assertEquals(balance, 500.00)  # replace with expected balance
