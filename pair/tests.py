from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from model_bakery import baker
from .models import Pair


class PairTests(TestCase):
        def setUp(self):
            self.pair = baker.make()
            print(self.pair.cost)