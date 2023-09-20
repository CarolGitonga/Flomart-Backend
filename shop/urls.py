from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter() #parent router

router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
#router.register('tags', views.TagViewSet)


product_router = routers.NestedDefaultRouter(router, 'products',lookup='product')#child router)
product_router.register('reviews', views.ReviewViewSet, basename='product_reviews')
urlpatterns=[
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('', include(product_router.urls))
]