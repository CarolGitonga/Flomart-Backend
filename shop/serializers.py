from rest_framework import serializers
from shop.models import Cart, Cartitems, Category, Product, Review



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
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','price']


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    sub_total = serializers.SerializerMethodField(method_name='total') 
    class Meta:
        model = Cartitems
        fields = ['id','cart','product','quantity', 'sub_total']  

    def total(self, cartitem:Cartitems):
        return cartitem.quantity * cartitem.product.price
        



class Cartserializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')
    class Meta:
        model = Cart
        fields = ['id', 'items', 'grand_total']

    def main_total(self, cart:Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total



