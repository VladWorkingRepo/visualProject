from rest_framework import status
from rest_framework.test import APITestCase

from CalculatorApp.models import Banks
from CalculatorApp.serializers import BanksSerializeModel


class BanksApiTestCase(APITestCase):
    def test_api_get_request(self):
        """Tests get request sent by the client.
        During regular work, the response status 200
        and a list with information "About banks" will be received"""

        bank_1 = Banks.objects.create(bank_name='Test First Bank', interest_rate=5.0)
        bank_2 = Banks.objects.create(bank_name='Test Second Bank', interest_rate=5.3)
        url = 'http://127.0.0.1:8000/api/banks/about/'
        response = self.client.get(url)
        serialized_data = BanksSerializeModel([bank_1, bank_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)
