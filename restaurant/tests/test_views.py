from restaurant.models import *
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'ksarthak4ever@gmail','hakunamatata','hakunamatata')
        self.client.force_authenticate(self.user)
    
        self.data = {'title': "IceCream", 'price': 80, 'inventory': 100}
       
    def test_create_menu(self):
        res = self.client.post('http://127.0.0.1:8000/api/menu-items/', self.data)
        self.assertEqual(res.status_code, 201)
    
    def test_getall(self):
        res = self.client.get('http://127.0.0.1:8000/api/menu-items/')
        self.assertEqual(res.status_code, 200)