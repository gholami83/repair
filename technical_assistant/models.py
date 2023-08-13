from django.db import models
from driver.models import Driver


class TechnicalAssistant(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    confirmed = models.BooleanField(default=False)