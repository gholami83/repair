from django.db import models
from driver.models import Driver


class Pair(models.Model):
    PAIR_CHOICES = Driver.objects.values_list('pair_description',flat=True)
    pair_request = models.CharField(max_length=50, choices=PAIR_CHOICES)
    date = models.DateField(auto_now_add=True)
    cost = models.BigIntegerField()
