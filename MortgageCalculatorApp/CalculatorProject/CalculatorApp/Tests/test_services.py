from django.test import TestCase

from CalculatorApp.services import data_for_client
from CalculatorApp.models import Banks


class ServicesTestCase(TestCase):
    def test_data_for_client(self):
        """Testing the main function that generates the final data.
        Once generated, the data is sent to the user."""
        bank_1 = Banks.objects.create(bank_name='Test First Bank', interest_rate=5.0)
        bank_2 = Banks.objects.create(bank_name='Test Second Bank', interest_rate=5.3)

        validate_data = {
                            'total_cost': 1000000,
                            'initial_fee': 500000,
                            'time': 10
                        }
        expected_value = [
                            {
                                "bank_name": "Test First Bank",
                                "annuity_payment": 5255,
                                "differential_payment": 6167,
                                "interest_rate": 5.0
                            },
                            {
                                "bank_name": "Test Second Bank",
                                "annuity_payment": 5255,
                                "differential_payment": 6167,
                                "interest_rate": 5.3
                            }
                        ]

        self.assertEqual(expected_value, data_for_client(validate_data))
