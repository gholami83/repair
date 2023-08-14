from django.db import models
from django.contrib.auth import get_user_model


class Driver(models.Model):
    driver = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    pair_description = models.TextField()
    def __str__(self):
        return str(self.pair_description)
    
    class Meta:
        db_table = 'pair_description' 