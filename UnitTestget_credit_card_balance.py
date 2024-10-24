
import unittest
from your_module import get_credit_card_balance

class TestGetCreditCardBalance(unittest.TestCase):
    def test_credit_card_balance(self):
        # Test with a valid customer ID
        result = get_credit_card_balance(1)
        self.assertEquals(result, 100.00)  # Assuming a balance of 100.00 for customer ID 1

    def test_no_credit_card_balance(self):
        # Test with a customer ID that has no credit card balance
        result = get_credit_card_balance(2)
        self.assertEquals(result, 0.00)

    def test_invalid_customer_id(self):
        # Test with an invalid customer ID
        result = get_credit_card_balance(-1)
        self.assertEquals(result, 0.00)

if __name__ == '__main__':
    unittest.main()
