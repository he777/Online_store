from django.db import models

from account.models import Account


class Category(models.Model):
    """
    Class to represent Category
    """
    name = models.CharField(max_length=200)
    comment = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Class to represent Product
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


STATUS = (
    ('star', 'started'),
    ('prog', 'in_progress'),
    ('canc', 'canceled'),
    ('fini', 'finished'))


class Order(models.Model):
    """
        Class to represent Order
    """
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default=Account)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)
    comment = models.CharField(blank=True, null=True, max_length=200)
    delivery_address = models.CharField(max_length=50)
    delivery_price = models.FloatField(default=2.90)
    date_of_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=4, default=STATUS[0][0])
    order_time = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return str(self.pk)

    @property
    def total_cost(self) -> float:
        """
         :rtype: float
         :returns: ordered product quantity multiplied by product item price
        """
        return self.quantity * self.product.price

    @property
    def delivery(self, delivery_price=2.90) -> float:
        """
            :type delivery_price: float
            :param delivery_price: default delivery expanse
            :rtype: float
            :returns: delivery price based on purchases sum
        """
        new_delivery_price = 0.0
        if self.total_cost > 50.0:
            return new_delivery_price
        else:
            return delivery_price

    @property
    def total(self) -> float:
        """
            :rtype: float
            :returns: total price for order
        """
        return self.delivery + self.total_cost
