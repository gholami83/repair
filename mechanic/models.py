from django.db import models
from django.contrib.auth import get_user_model


class Mechanic(models.Model):
    mechanic = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    class Meta:
        db_table = 'mechanic' 
    