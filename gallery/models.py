from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def _str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def _str__(self):
        return self.name

class Image(models.Model):
    image=models.ImageField(upload_to='photos/')
    image_name=models.CharField(max_length=30)
    image_description=models.CharField(max_length=60)
    location=models.ForeignKey('Location')
    category=models.ForeignKey('Category')

    def _str__(self):
        return self.name

    @classmethod
    def search_by_category(cls,search_term):
        images=cls.objects.filter(category__name__icontains=search_term)
        return images
    # @classmethod
    # def get_all(cls):
    #
    #  images = cls.objects.all()
    #  return images
