from django.db import models

# Image
# Image Name.
# Image Description.
# Image Location Foreign Key.
# Image category Foreign Key.

class Location(models.Model):
    location=models.CharField(max_length=30)
class Category(models.Model):
    category=models.CharField(max_length=30)
class Image(models.Model):
    image=models.ImageField(upload_to='photos/')
    image_name=models.CharField(max_length=30)
    image_description=models.CharField(max_length=60)
    location=models.ForeignKey(Location)
    category=models.ForeignKey(Category)
