from product.models import Product, Category
from rest_framework import generics
from .serializer import ProductSerializer
from .serializer import CategoriesSerializer

from rest_framework.generics import RetrieveAPIView


class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailViewSet(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoriesViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class CategoriesDetailViewSet(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
