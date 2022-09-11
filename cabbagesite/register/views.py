from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from register.forms import UserRegisterForm, UserLoginForm


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная регистрация')
            return redirect('promout')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('stat')
    else:
        form = UserLoginForm()
    return render(request, 'register/login.html', {'form': form})
