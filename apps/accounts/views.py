from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             #  log the user in
             login(request, user)
             return redirect('accounts/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/singup.html, { 'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form})

def logout(request):
    if request.method == 'POST':
            logout(request)
            return redirect('accounts/login.html')
