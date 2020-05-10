from rest_framework import status
from rest_framework.test import APITestCase

from product.models import Order


class CategoryTests(APITestCase):

    def test_create_order(self):
        """
        Creates a Order object
        """
        # given
        url = '/api/orders/'

        data = {'user': '1', 'delivery_address': 'Maaküla 12, Tallinn', 'date_of_order': '2020-05-09T19:38:57.350531Z',
                'status': 'star', 'order_time': '2020-05-09T19:38:57.350572Z', 'delivery': 2.90, 'total_cost': 35.0}

        # when
        response = self.client.post(url, data, format='json')

        # assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().user, '1')
        self.assertEqual(Order.objects.get().date_of_order, '2020-05-09T19:38:57.350531Z')
        self.assertEqual(Order.objects.get().status, 'star')
        self.assertEqual(Order.objects.get().order_time, '2020-05-09T19:38:57.350572Z')
        self.assertEqual(Order.objects.get().delivery, 2.90)
        self.assertEqual(Order.objects.get().total_cost, 36.0)
