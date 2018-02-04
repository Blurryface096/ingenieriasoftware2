from django.contrib import admin
from .models import Preguntas
from .models import Juego
from .models import Partido
from .models import ParticipacionPolla
from .models import Equipo
from .models import Formaciones
from .models import Jugador

admin.site.register(Preguntas)
admin.site.register(Juego)
admin.site.register(Partido)
admin.site.register(ParticipacionPolla)
admin.site.register(Equipo)
#admin.site.register(Formaciones)
#admin.site.register(Jugador)
