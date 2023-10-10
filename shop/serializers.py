from rest_framework import serializers
from django.db import transaction
from shop.models import Cart, Cartitems, Category, Order, OrderItem, Product, Review



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
    
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','price']


class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(many=False)
    sub_total = serializers.SerializerMethodField(method_name='total') 
    class Meta:
        model = Cartitems
        fields = ['id','cart','product','quantity', 'sub_total']  

    def total(self, cartitem:Cartitems):
        return cartitem.quantity * cartitem.product.price
    
class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('There is no product associated with the given ID')
        return value
        
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        try:
            cartitem = Cartitems.objects.get(product_id =product_id, cart_id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()

            self.instance = cartitem
        except:
            self.instance = Cartitems.objects.create(cart_id=cart_id, **self.validated_data)

        return self.instance
    class Meta:
        model = Cartitems
        fields = ['id','product_id', 'quantity']
        
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['quantity']



class Cartserializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ['id', 'items', 'grand_total']

    def main_total(self, cart: Cart):
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total
    
class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id','product','quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id','placed_at','pending_status','owner','items']

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('This cart_id is invalid')
        
        elif not Cartitems.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError('Sorry your cart is empty')
        return cart_id

    #customize the serializer save method
    def save(self, **kwargs):
        with transaction.atomic():
           cart_id = self.validated_data['cart_id']
           user_id = self.context['user_id']
           order = Order.objects.create(owner_id = user_id)
           cartitems = Cartitems.objects.filter(cart_id=cart_id)
           orderitems = [
               OrderItem(
                   order=order,
                   product=item.product,
                   quantity=item.quantity
               )
            for item in cartitems
           ]
           OrderItem.objects.bulk_create(orderitems)
           return order
        


