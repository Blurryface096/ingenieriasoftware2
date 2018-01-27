from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.home.models import Preguntas

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def trivia(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'home/trivia.html')
