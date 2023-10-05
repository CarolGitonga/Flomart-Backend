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
    """
    Serializer class for serializing and deserializing instances of the Cart model.
    Includes a nested serializer for the CartItem model and calculates the total price of all items in the cart.
    """

    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Cart
        fields = ['id', 'items', 'grand_total']

    def main_total(self, cart: Cart):
        """
        Calculates the total price of all items in the cart.

        Parameters:
        - cart: The Cart instance for which to calculate the total price.

        Returns:
        - The total price of all items in the cart.
        """
        items = cart.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total



