from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Stores a a Category model, related to Product
    """
    name = models.CharField(max_length=200)
    parent_id = models.CharField(max_length=20)
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
    price = models.DecimalField(decimal_places=0, max_length=10, max_digits=10)
    product_type = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    comment = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.name
