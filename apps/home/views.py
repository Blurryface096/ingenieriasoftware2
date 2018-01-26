from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def cerrar_sesion(request):
    if request.method == 'GET':

        return redirect('/login/login.html')
    else:

        return render(request, 'login/login.html', {'form':form})
