# Generated by Django 2.2.5 on 2020-04-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20200406_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='老师点评'),
        ),
    ]