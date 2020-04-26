from django.urls import path

from rest_framework import routers
from .api import CategoriesViewSet  # CategoriesDetailViewSet, ProductViewSet, ProductDetailViewSet

router = routers.DefaultRouter()
router.register('api/categories', CategoriesViewSet, 'categories')

urlpatterns = router.urls

"""
urlpatterns = [
    # path('api/products', ProductViewSet.as_view()),
    # path('api/product/<pk>', ProductDetailViewSet.as_view()),
    path('api/categories/', CategoriesViewSet.as_view()),
    # path('api/category/<pk>', CategoriesDetailViewSet.as_view())
]
"""