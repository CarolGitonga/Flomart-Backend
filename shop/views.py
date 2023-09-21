from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from shop.filters import ProductFilter
from shop.models import Product, Category,  Review
from .serializers import ProductSerializer, CategorySerializer,  ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ProductViewSet(ModelViewSet):
    queryset = products = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends =[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price']
    pagination_class = PageNumberPagination

class CategoryViewSet(ModelViewSet):
    queryset = products = Category.objects.all()
    serializer_class = CategorySerializer

#class TagViewSet(ModelViewSet):
    #queryset = products = Tag.objects.all()
   # serializer_class = TagSerializer

class ReviewViewSet(ModelViewSet):
    #queryset = products = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        Review.objects.filter(product_id = self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


