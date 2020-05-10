from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product, Category
from account.models import Account


class CategoryTests(APITestCase):
    
    def test_create_category(self):
        """
        Creates a category object
        """
        # given
        url = '/api/categories/'
        
        data = {'name': 'Category 1', 'comment': 'This is one category'}

        # when
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Category 1')
        self.assertEqual(Category.objects.get().comment, 'This is one category')


class ProductFilterTests(APITestCase):

    def setUp(self):

        user1 = Account.objects.create_user(email="user1@user1.com", username="user1", password="ewfewfwg21@")
        
        category1 = Category.objects.create(name="Category 1")
        category2 = Category.objects.create(name="Category 2")

        Product.objects.create(name="Product 1", price=1, author=user1, category=category1)
        Product.objects.create(name="Another 2", price=1, author=user1, category=category2)

    def test_filtering_by_category(self):

        # given
        url = '/api/products/'

        data = {'category': 2}

        # when
        response = self.client.get(url, data)

        json = response.json()

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json), 1)
        self.assertEqual(json[0]["name"], "Another 2")

    def test_filtering_by_name(self):

        # given
        url = '/api/products/'

        data = {'name__istartswith': 'Product'}

        # when
        response = self.client.get(url, data)

        json = response.json()

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(json), 1)
        self.assertEqual(json[0]["name"], "Product 1")
