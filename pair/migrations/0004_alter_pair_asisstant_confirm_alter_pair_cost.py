# Generated by Django 4.2.4 on 2023-08-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pair', '0003_pair_asisstant_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='asisstant_confirm',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='pair',
            name='cost',
            field=models.BigIntegerField(blank=True),
        ),
    ]