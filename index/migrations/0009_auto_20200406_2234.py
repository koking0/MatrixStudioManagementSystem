# Generated by Django 2.2.5 on 2020-04-06 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20200406_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='学生'),
        ),
    ]