# Generated by Django 2.0.1 on 2018-02-03 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180203_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='organizador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='home.Usuario'),
            preserve_default=False,
        ),
    ]
