
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from shop.filters import ProductFilter
from shop.models import Cart, Product, Category, Review
from .serializers import Cartserializer, ProductSerializer, CategorySerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin

# Create your views here
class ProductViewSet(ModelViewSet):
    queryset = products = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends =[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price']
    pagination_class = PageNumberPagination

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#class TagViewSet(ModelViewSet):
    #queryset = products = Tag.objects.all()
   # serializer_class = TagSerializer

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
         return Review.objects.filter(product_id=self.kwargs["product_pk"])
    
    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
8


class CartViewset(CreateModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = Cartserializer
