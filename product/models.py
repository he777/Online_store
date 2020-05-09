from django.db import models

import product
from account.models import Account


class Category(models.Model):
    """
    Stores a a Category model, related to Product
    """
    name = models.CharField(max_length=200)
    comment = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Stores a a Products model, related to Category
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=3000)
    image_url = models.URLField(max_length=1000)
    inventory = models.CharField(max_length=300)
    price = models.FloatField()
    comment = models.CharField(blank=True, null=True, max_length=200)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    comment = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return str(self.product)

    @classmethod
    def total_cost(cls):
        return cls.quantity * cls.product.price


STATUS = (
    ('str', 'started'),
    ('prog', 'in_progress'),
    ('can', 'canceled'),
    ('fin', 'finished'))


class Order(models.Model):
    """
        Stores Order model
    """
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=50)
    delivery_price = models.FloatField(default=2.90)
    date_of_order = models.DateTimeField(auto_now_add=True)
    order_lines = models.ManyToManyField(OrderItem)
    status = models.CharField(choices=STATUS, max_length=4, default=STATUS[0][0])
    order_time = models.DateTimeField(blank=True, auto_now=True)
    comment = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return str(self.pk)

    @property
    def price(self):
        if OrderItem.total_cost.__ge__(50.0):
            self.delivery_price = 0
            return self.delivery_price

    @property
    def total(self):
        return self.price + OrderItem.total_cost()
