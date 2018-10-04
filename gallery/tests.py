from django.test import TestCase
from .models import Image,Location,Category

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location=Location(name='Ngong')
    def tearDown(self):
        Location.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))
    def test_save_location(self):
        self.new_location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)
    def test_delete_location(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        location=Location.objects.all()
        self.assertEqual(len(location),0)
    def test_update_location(self):
        self.new_location.save_location()
        self.new_location.update_locations(name='Kenya')
        self.assertEqual(self.new_location.name,'Kenya')

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category=Category(name='Nature')
    def tearDown(self):
        Category.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))
    def test_save_category(self):
        self.new_category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)
    def test_delete_category(self):
        self.new_category.save_category()
        self.new_category.delete_category()
        category=Category.objects.all()
        self.assertEqual(len(category),0)
    def test_update_category(self):
        self.new_category.save_category()
        self.new_category.update_category(name='sports')
        self.assertEqual(self.new_category.name,'sports')
class ImageTestClass(TestCase):
    def setUp(self):
        self.new_image=Image(name='hazard')
    def tearDown(self):
        Image.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    def test_save_image(self):
        self.new_image.save_image()
        image=Image.objects.all()
        self.assertTrue(len(image)>0)
    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        image=Image.objects.all()
        self.assertEqual(len(image),0)
    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image(name='flask')
        self.assertEqual(self.new_image.name,'flask')
