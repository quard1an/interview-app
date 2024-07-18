from django.test import TestCase
from .models import Item
from django.test import override_settings
from .tasks import add

class ItemModelTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="Test Item", price=10.00)

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.price, 10.00)


class CeleryTaskTest(TestCase):


    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_celery_task_add(self):
        result = add.delay(5,10)
        self.assertTrue(result.success())

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_celery_task_add(self):
        result = add.delay(5,10)
        self.assertEqual(15, result.get())

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_celery_task_add(self):
        result = add.delay('a', 'b')
        self.assertRaises(Exception, result)
    

