from rest_framework import serializers
from product.models import Category, Product, OrderItem, Order


class CategoriesSerializer(serializers.ModelSerializer):
    '''url = serializers.HyperlinkedIdentityField(
        view_name='CategoriesDetailViewSet',
        lookup_field='pk',
    )'''

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    total_cost = serializers.FloatField()

    class Meta:
        model = OrderItem
        fields = ('user', 'product', 'quantity', 'comment', 'total_cost')


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.FloatField()

    class Meta:
        model = Order
        fields = ('user', 'delivery_address', 'date_of_order', 'order_lines', 'status', 'order_time', 'comment', 'total')