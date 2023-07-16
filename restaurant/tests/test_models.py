from restaurant.models import *
from django.test import TestCase

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        output_str = f'{item.title} : {str(item.price)}'
        self.assertEqual(output_str, "IceCream : 80")