from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', {'message': 'Listado de productos', 'title': 'Productos', 'products': [

        {'title': 'Playera', 'price': 5, 'stock': True},
        {'title': 'Remera', 'price': 4, 'stock': True},
        {'title': 'Camisa', 'price': 7, 'stock': False},
        {'title': 'Zapatillas', 'price': 9, 'stock': True}

    ]})


def login_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        # EN CASO NO HUBIESE UNA CUENTA ASI, DEVUELVE NONE
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
    return render(request, 'users/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente. ')
    return redirect('login')


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('index')
    return render(request, 'users/register.html', {'form': form})
