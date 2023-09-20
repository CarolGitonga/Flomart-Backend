from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from shop.models import Product, Category,  Review
from .serializers import ProductSerializer, CategorySerializer,  ReviewSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ProductViewSet(ModelViewSet):
    queryset = products = Product.objects.all()
    serializer_class = ProductSerializer

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


