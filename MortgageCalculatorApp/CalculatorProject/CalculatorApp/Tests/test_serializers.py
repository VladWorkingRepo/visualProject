from django.test import TestCase

from CalculatorApp.serializers import *


class SerializersTestCase(TestCase):
    def test_banks_serializer(self):
        """This test checks what data the BanksSerializeModel should return"""
        bank_1 = Banks.objects.create(bank_name='Test First Bank', interest_rate=5.0)
        bank_2 = Banks.objects.create(bank_name='Test Second Bank', interest_rate=5.3)
        sent_data = BanksSerializeModel([bank_1, bank_2], many=True).data
        expected_data = [
            {
                'id': bank_1.id,
                'bank_name': 'Test First Bank',
                'interest_rate': 5.0
            },
            {
                'id': bank_2.id,
                'bank_name': 'Test Second Bank',
                'interest_rate': 5.3
            }
        ]
        self.assertEqual(expected_data, sent_data)

    def test_data_client_serializer(self):
        """This test checks what data the DataClientSerializeModel should return"""
        request_body = {
                            "total_cost": "1000000",
                            "initial_fee": "500000",
                            "time": "10"
                        }

        expected_data = {
                            'total_cost': 1000000,
                            'initial_fee': 500000,
                            'time': 10
                        }
        checked_serializer = DataClientSerializeModel(request_body).data
        self.assertEqual(expected_data, checked_serializer)

