from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    


    def __str__(self):
        return self.title

#class Tag(models.Model):
    #name = models.CharField(max_length=200)

    #def __str__(self):
        #return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=True, blank=True)
    #tags = models.ManyToManyField(Tag)
    color = models.CharField(max_length=50)
    #stock_quantity = models.PositiveIntegerField()
    date_added = models.DateField()
    featured = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)



    def __str__(self):
        return self.title
    
class Review(models.Model):
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5),MinValueValidator(1)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='post_comment')
    purchased = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    