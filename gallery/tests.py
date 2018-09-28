from django.test import TestCase
from .models import Image,Location,Category

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location=Location(name='Ngong')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))
    def test_save_location(self):
        self.new_location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category=Category(name='Nature')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))
    def test_save_category(self):
        self.new_category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)
