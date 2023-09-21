from rest_framework import serializers
from shop.models import Category, Product, Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','category','image','price','color','date_added','featured']

#class TagSerializer(serializers.ModelSerializer):
    #class Meta:
       # model = Tag
       # fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','title','description','rating','date_added']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id, **validated_data)
    
    class SimpleProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['id', 'title', 'price']
        

