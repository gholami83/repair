from rest_framework.test import APIRequestFactory


factory  =APIRequestFactory()
request = factory.post('', {'username':'ali','password':'1'})