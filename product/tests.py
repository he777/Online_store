from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Product


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
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Category 1')
        self.assertEqual(Product.objects.get().comment, 'This is one category')
