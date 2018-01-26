from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def trivia(request):
    preguntas = Preguntas.objects.all()
    return render(request, 'home/trivia.html')
