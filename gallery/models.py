from django.db import models

# Image
# Image Name.
# Image Description.
# Image Location Foreign Key.
# Image category Foreign Key.

class Location(models.Model):
    name=models.CharField(max_length=30)

    def save_location(self):
        self.save()

class Category(models.Model):
    name=models.CharField(max_length=30)

    def save_category(self):
        self.save()

class Image(models.Model):
    image=models.ImageField(upload_to='photos/')
    image_name=models.CharField(max_length=30)
    image_description=models.CharField(max_length=60)
    location=models.ForeignKey(Location)
    category=models.ForeignKey(Category)
