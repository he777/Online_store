from rest_framework import generics, viewsets, permissions

from product.models import Category
from .serializer import CategoriesSerializer

# from .serializer import ProductSerializer
# from product.models import Product

from rest_framework.generics import RetrieveAPIView

"""
class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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