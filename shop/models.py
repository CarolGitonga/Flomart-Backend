from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    


    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', blank=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    color = models.CharField(max_length=50)
    stock_quantity = models.PositiveIntegerField()
    date_added = models.DateField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    