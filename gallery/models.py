from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_locations(self):
        self.delete()

    def update_locations(self):
        self.update( )

    def _str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

    def _str__(self):
        return self.name

class Image(models.Model):
    image=models.ImageField(upload_to='photos/')
    image_name=models.CharField(max_length=30)
    image_description=models.CharField(max_length=60)
    location=models.ForeignKey('Location')
    category=models.ForeignKey('Category')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update( )

    @classmethod
    def search_by_category(cls,search_term):
        images=cls.objects.filter(category__name__icontains=search_term)
        return images
    @classmethod
    def filter_by_location(cls , location):
        locations=cls.objects.filter( location=location )
        return locations

    @classmethod
    def get_image_by_id(cls):
        Image.cls.objects.filter( id )
        return Image
