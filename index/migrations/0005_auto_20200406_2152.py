# Generated by Django 2.2.5 on 2020-04-06 13:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200406_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='achievement',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='成绩'),
        ),
    ]
