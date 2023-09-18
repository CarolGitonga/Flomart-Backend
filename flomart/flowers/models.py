from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    
class Product(models.Model):
    #name, description, price, image(s), category, color, stock quantity,
    #  date added, featured status.
    #  Relationships: Many-to-many relationship with categories and tags.
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', blank=True)
    category = models.ForeignKey(Category, related_name='flowers', on_delete=models.CASCADE)

