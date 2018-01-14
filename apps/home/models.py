from django.db import models

# Create your models here.
class Juego(models.Model):
    nombre = models.CharField(max_length=15)
    modo = models.IntegerField()
