from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from CalculatorApp.models import Banks
from CalculatorApp.serializers import BanksSerializeModel


class ApiTestCase(APITestCase):
    def setUp(self):
        superuser = User.objects.create_superuser(
            username='TestSuperuser',
            password='TestPassword'
        )
        superuser.save()
        self.client.login(username='TestSuperuser', password='TestPassword')

    def test_api_post_request(self):
        url = 'http://127.0.0.1:8000/api/banks/about/'

        data = {
                    "bank_name": "FIRST SENT",
                    "interest_rate": 5.0
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_put_request(self):
        banks = Banks.objects.create(bank_name='Test Bank Record', interest_rate=5.0)
        url = f'http://127.0.0.1:8000/api/banks/about/{banks.id}/'
        data = {
                    "bank_name": "Changed Bank",
                    "interest_rate": 6.0
                }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_delete_request(self):
        banks = Banks.objects.create(bank_name='Test First Bank', interest_rate=5.0)
        url = f'http://127.0.0.1:8000/api/banks/about/{banks.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.client.logout()

    def test_api_get_request(self):
        bank_1 = Banks.objects.create(bank_name='Test First Bank', interest_rate=5.0)
        bank_2 = Banks.objects.create(bank_name='Test Second Bank', interest_rate=5.3)
        url = 'http://127.0.0.1:8000/api/banks/about/'
        response = self.client.get(url)
        serialized_data = BanksSerializeModel([bank_1, bank_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serialized_data, response.data)
