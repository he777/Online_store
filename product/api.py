from rest_framework import generics, viewsets, permissions

from product.models import Category, Product
from .serializer import CategoriesSerializer, ProductSerializer

from rest_framework.generics import RetrieveAPIView


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer

"""
class ProductDetailViewSet(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
"""


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriesSerializer


"""
class CategoriesDetailViewSet(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
"""