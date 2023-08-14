from django.db import models
from driver.models import Driver


class Pair(models.Model):
    pair_request = models.OneToOneField(Driver,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    cost = models.BigIntegerField(null=True, blank=True)
    asisstant_confirm = models.BooleanField(default=False,blank=True)   
    