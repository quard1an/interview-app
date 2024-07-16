from django.test import TestCase
from .models import Item

class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="Test Item", price=10.00)

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.price, 10.00)
