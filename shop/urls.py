from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter() #parent router

router.register("products", views.ProductViewSet)
router.register("categories", views.CategoryViewSet)
router.register("carts", views.CartViewset)
product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

urlpatterns = router.urls


urlpatterns=[
    path('', include(router.urls)),
    path('', include(product_router.urls))
]