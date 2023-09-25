from rest_framework import serializers
from shop.models import Cart, Category, Product, Review



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title', 'slug','description','category','image','price','color','date_added','featured']

    category = CategorySerializer(read_only=True)# to prevent unnecessary write operations


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name','description','date_added']

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(product_id = product_id,  **validated_data)
    
   
    #def create(self, validated_data):
       # product_id = self.context["product_id"]
       # validated_data.pop('product', None)  # Remove 'product' from validated_data
       # return Review.objects.create(product_id=product_id, **validated_data)
        
class Cartserializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ['id']

