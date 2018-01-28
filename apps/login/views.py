from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from apps.login.forms import UsuarioForm


# Create your views here.
def index(request):
    return render(request, 'login/login.html')

def ingresar(request):
    estado=True
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:

        login(request, user)
        return redirect('/home:index')
    else:
        form = UsuarioForm()
        estado=False
    return render(request, 'login/login.html', {'form':form,'estado':estado})
