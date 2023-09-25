from rest_framework import serializers
from shop.models import Category, Product, Review



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)# to prevent unnecessary write operations
    class Meta:
        model = Product
        fields = ['id','title','description','category','image','price','color','date_added','featured']

    


class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Review
        fields = ['id','name','description','date_added','product']

    #def create(self, validated_data):
       # product_id = self.context["product_id"]
        #return Review.objects.create(product_id = product_id,  **validated_data)
    
    #def create(self, validated_data):
        #product_data = validated_data.pop('product')
        #product_id = self.context.get('product_id')
        #review = Review.objects.create(product_id=product_id, **validated_data)
        #return review
    def create(self, validated_data):
        product_id = self.context["product_id"]
        validated_data.pop('product', None)  # Remove 'product' from validated_data
        return Review.objects.create(product_id=product_id, **validated_data)
        

