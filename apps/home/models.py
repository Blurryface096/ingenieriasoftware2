from django.db import models
from django.forms import ModelForm

# Create your models here.

TIPO_JUEGOS = (
    ('Polla','Polla'),
    ('Trivia','Trivia'),
    ('Equipo','Equipo Ideal'),
)

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    tipo = models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.username)


class Juego(models.Model):

    nombre = models.CharField(max_length=15)
    n_jugadores=models.PositiveIntegerField()
    #tipo=ModelForm.ModelChoiceField(queryset=TIPO_JUEGOS, empty_label='Trivia')
    tipo = models.CharField(max_length=15, choices=TIPO_JUEGOS)
    organizador=models.ForeignKey(Usuario, related_name='usuario', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class JuegoForm(ModelForm):
    class Meta:
        model=Juego
        fields=['nombre', 'n_jugadores','tipo']


class CrearForm(ModelForm):
    class Meta:
        pass



class Preguntas(models.Model):
    pregunta = models.CharField(max_length = 500)
    opcion1 = models.CharField(max_length = 20)
    opcion2 = models.CharField(max_length = 20)
    opcion3 = models.CharField(max_length = 20)
    opcion4 = models.CharField(max_length = 20)
    respuesta = models.CharField(max_length = 20)

    def __str__(self):
        return self.pregunta


class Demarcacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)




class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, related_name='equipo', on_delete=models.CASCADE)
    demarcacion = models.ForeignKey(Demarcacion, related_name='Demarcacion', on_delete=models.CASCADE, blank=True, null=True)
    ataque = models.PositiveIntegerField()
    defensa = models.PositiveIntegerField()
    velocidad = models.PositiveIntegerField()

    def __str__(self):
        return '{} {} | {}'.format(self.nombre, self.apellido, self.demarcacion)

class Formaciones(models.Model):
    cantidad_arqueros = models.PositiveIntegerField()
    cantidad_defensas = models.PositiveIntegerField()
    cantidad_centrocampistas = models.PositiveIntegerField()
    cantidad_delanteros = models.PositiveIntegerField()

    def __str__(self):
        return '{} - {} - {}'.format(self.cantidad_defensas, self.cantidad_centrocampistas, self.cantidad_delanteros)

class ParticipacionEquipoIdeal(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ataque = models.FloatField()
    defensa = models.FloatField()
    velocidad = models.FloatField()
    total = models.FloatField()
    fecha = models.DateTimeField()
    juego=models.ForeignKey(Juego, on_delete=models.CASCADE)

    def __str__(self):
        return '{} / {}'.format(self.usuario, self.fecha)




class Partido(models.Model):
    eq_local = models.ForeignKey(Equipo, related_name='equipo_local', on_delete=models.CASCADE)
    eq_visita = models.ForeignKey(Equipo, related_name='equipo_visita', on_delete=models.CASCADE)
    resultado = models.PositiveIntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return '{} vs {}'.format(self.eq_local, self.eq_visita)

class ParticipacionPolla(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    score = models.IntegerField()
    fecha = models.DateTimeField()
    juego=models.ForeignKey(Juego, on_delete=models.CASCADE)
    def __str__(self):
        return '{} / {}'.format(self.usuario, self.fecha)

class Polla(models.Model):
    participacion = models.ForeignKey(ParticipacionPolla, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    resultado = models.PositiveIntegerField()
    juego=models.ForeignKey(Juego, on_delete=models.CASCADE)
