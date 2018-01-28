from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.login.forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request, 'login/login.html')

def ingresar(request):
    estado=True
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            print ("Formulario valido")
        return redirect('/home:index')
    else:
        form = UsuarioForm()
        estado=False
    return render(request, 'login/login.html', {'form':form,'estado':estado})
