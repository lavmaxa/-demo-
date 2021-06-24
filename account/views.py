from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from .forms import *

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                    login(request, user)
                    return render(request, 'account/account.html')
            else:
                return render(request, 'account/account.html', {'form': form,'login_error' : "Неверный логин или пароль "})
    else:
        form = LoginForm()
    return render(request, 'account/account.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect("index")

