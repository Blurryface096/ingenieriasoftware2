from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from apps.home.models import CrearForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             #  log the user in
             login(request, user)
             return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/singup.html', { 'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            crear=CrearForm
            return redirect('home:index', { 'crear': crear})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form})

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('accounts:login')
