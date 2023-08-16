from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import response
from rest_framework.test import APITestCase
from .models import Driver


class DriverTest(APITestCase):

    # def test_create_user(self):
    #     url = reverse('authuser')
    #     data = {
    #         'username':'amir',
    #         'password' : '1',
    #     }
    #     self.client.post(url,data,format= 'json') 

    def test_create_driver(self):
        # url = reverse('authuser')
        # data = {
        #     'username':'amir',
        #     'password' : '1',
        # }
        # self.client.post(url,data,format= 'json') 

        url = reverse('driver-list')
        data = {
            'driver': get_user_model().objects.create(),
            'pair_description': 'this is my report',
        }
        response = self.client.post(url,data)

        # self.assertEqual(response.data.get("driver"),None\])
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Driver.objects.count(),1)
        self.assertEqual(Driver.objects.get(driver = 1).pair_description,'this is my report')   