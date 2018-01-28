from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.home.models import Preguntas
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url="/accounts/login/")
def trivia(request):
    preguntas = Preguntas.objects.all()
    return render(request, 'home/trivia.html', { 'preguntas': preguntas})
