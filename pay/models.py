from django.db import models


class Pay(models.Model):
    payed = models.BooleanField(default=False)
    cost = models.BigIntegerField()
    resault = models.TextField()
    date = models.DateField(auto_now_add= False)
