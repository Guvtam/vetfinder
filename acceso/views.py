from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, MascotaForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages




def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas o usuario desactivado.')
    else:
        form = AuthenticationForm()
    return render(request, 'acceso/login.html', {'form': form})
    

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('agregar_mascota')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'acceso/signup.html', {'form': form})


def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.dueno = request.user  
            mascota.save()
            return redirect('home')  
    else:
        form = MascotaForm()
    return render(request, 'acceso/registroMascota.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')


