from django.db import models

# Create your models here.
class Usuario(models.Model):
    email = models.CharField(max_length=10)
    contra = models.CharField(max_length=10)
    tipo = models.IntegerField()
