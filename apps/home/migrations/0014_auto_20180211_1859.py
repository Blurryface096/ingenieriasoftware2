# Generated by Django 2.0.1 on 2018-02-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180211_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='estado',
            field=models.CharField(blank=True, choices=[('Abierto', 'Abierto'), ('Cerrado', 'Cerrado')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='juego',
            name='privacidad',
            field=models.CharField(blank=True, choices=[('Privado', 'Privado'), ('Publico', 'Publico')], max_length=15, null=True),
        ),
    ]
