from django.db import models
from django.contrib.auth import get_user_model


class TechnicalAssistant(models.Model):
    assistant = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    class Meta:
        db_table = 'assistant' 