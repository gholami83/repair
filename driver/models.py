from django.db import models
from django.contrib.auth import get_user_model


class Driver(models.Model):
    driver = models.OneToOneField(get_user_model(),models.CASCADE)
    pair_description = models.TextField()