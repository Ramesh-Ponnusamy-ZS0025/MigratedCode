
import unittest
from your_module import count_late_payments  # Replace with the actual module name

class TestCountLatePayments(unittest.TestCase):
    def test_late_payments_found(self):
        # Arrange
        customer_id = 123  # Existing customer ID with late payments
        expected_late_pay_count = 2  # Expected count of late payments for this customer

        # Act
        late_pay_count = count_late_payments(customer_id)

        # Assert
        self.assertEquals(late_pay_count, expected_late_pay_count)

    def test_no_late_payments_found(self):
        # Arrange
        customer_id = 456  # Existing customer ID with no late payments
        expected_late_pay_count = 0  # Expected count of late payments for this customer

        # Act
        late_pay_count = count_late_payments(customer_id)

        # Assert
        self.assertEquals(late_pay_count, expected_late_pay_count)

    def test_nonexistent_customer(self):
        # Arrange
        customer_id = 789  # Non-existent customer ID
        expected_late_pay_count = 0  # Expected count of late payments for this non-existent customer

        # Act
        late_pay_count = count_late_payments(customer_id)

        # Assert
        self.assertEquals(late_pay_count, expected_late_pay_count)

if __name__ == '__main__':
    unittest.main()
