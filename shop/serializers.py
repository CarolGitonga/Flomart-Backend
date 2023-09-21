from rest_framework import serializers
from shop.models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','category','image','price','color','date_added','featured']

    category = CategorySerializer()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','title','description','rating','date_added']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id, **validated_data)
    
    
        

