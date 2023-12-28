from django.test import TestCase
from restaurant.models import Menu
from django.test import Client

from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        # Add a client.
        self.client = Client()

        # Create a sample Menu instance for testing
        self.menu_item = Menu.objects.create(name='Sample Item', price=10.0)

    def test_getItem(self):
        response = self.client.get(f'/menu/{self.menu_item.id}/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the JSON response content type:
        self.assertEqual(response['Content-Type'], 'application/json')

        # You can also assert specific data in the response content:
        expected_data = MenuSerializer(instance=self.menu_item).data
        self.assertEqual(response.json(), expected_data)

    def test_getall(self):
        response = self.client.get('/menu/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the length:
        self.assertEqual(len(response.json()), Menu.objects.count())
