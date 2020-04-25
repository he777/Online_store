from django.urls import path

from .api import ProductViewSet, ProductDetailViewSet, CategoriesViewSet, CategoriesDetailViewSet

urlpatterns = [
    path('api/products', ProductViewSet.as_view()),
    path('api/product/<pk>', ProductDetailViewSet.as_view()),
    path('api/categories/', CategoriesViewSet.as_view()),
    path('api/category/<pk>', CategoriesDetailViewSet.as_view())
]