from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter() #parent router

router.register("products", views.ProductViewSet)
router.register("categories", views.CategoryViewSet)
router.register("carts", views.CartViewset)
router.register("orders", views.OrderViewSet, basename="orders")
router.register("n_profiles", views.ProfileViewSet)


product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-reviews")
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewset, basename='cart-items')



urlpatterns=[
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls))
]