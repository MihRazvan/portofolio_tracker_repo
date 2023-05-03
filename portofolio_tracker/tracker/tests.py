# myapp/tests.py
from django.test import TestCase

class MyModelTestCase(TestCase):
    def test_model_str(self):
        my_model = MyModel.objects.create(name='Test', description='This is a test')
        self.assertEqual(str(my_model), 'Test')