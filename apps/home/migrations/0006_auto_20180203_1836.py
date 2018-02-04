# Generated by Django 2.0.1 on 2018-02-03 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_juego_organizador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='organizador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]