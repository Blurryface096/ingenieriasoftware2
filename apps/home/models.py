from django.db import models

# Create your models here.
class Juego(models.Model):
    nombre = models.CharField(max_length=15)
    modo = models.IntegerField()


class Preguntas(models.Model):
    pregunta = models.CharField(max_length = 500)
    opcion1 = models.CharField(max_length = 20)
    opcion2 = models.CharField(max_length = 20)
    opcion3 = models.CharField(max_length = 20)
    opcion4 = models.CharField(max_length = 20)
    respuesta = models.CharField(max_length = 20)

    def __str__(self):
        return self.pregunta
