from django.urls import include, path

from rest_framework import routers
from .api import CategoriesViewSet, ProductViewSet  # CategoriesDetailViewSet, ProductViewSet, ProductDetailViewSet

router = routers.DefaultRouter()
router.register('api/categories', CategoriesViewSet, 'categories')
router.register('api/products', ProductViewSet, 'products')


urlpatterns = [
    path('', include(router.urls)),
    # path('api/product/<pk>', ProductDetailViewSet.as_view()),
    # path('api/categories/', CategoriesViewSet.as_view()),
    # path('api/category/<pk>', CategoriesDetailViewSet.as_view())
]
