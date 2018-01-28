from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.home.models import Preguntas
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required(login_url='/')
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url='/')
def trivia(request):
    preguntas = Preguntas.objects.all()

    return render(request, 'home/trivia.html', { 'preguntas': preguntas})

def logout_view(request):
    logout(request)


def signup_view(request):

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:


        form=UserCreationForm()
    return render(request,'accounts/signup.htlm',{'form':form})
