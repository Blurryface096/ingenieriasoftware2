# Generated by Django 2.0.1 on 2018-02-04 01:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_auto_20180203_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='invitados',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
