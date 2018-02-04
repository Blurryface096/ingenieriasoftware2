from django.contrib import admin
from .models import Preguntas
from .models import Juego
from .models import Partido
from .models import ParticipacionPolla
from .models import Equipo

admin.site.register(Preguntas)
admin.site.register(Juego)
admin.site.register(Partido)
admin.site.register(ParticipacionPolla)
admin.site.register(Equipo)
