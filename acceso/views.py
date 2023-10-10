from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, MascotaForm, LoginForm, TipoUsuarioForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Mascota , TipoUsuario



def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Credenciales inválidas o usuario desactivado.')
    else:
        form = LoginForm()
    return render(request, 'acceso/login.html', {'form': form})

    

def registro_dueno_mascota(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            captcha_response = request.POST.get('g-recaptcha-response')
            if not captcha_response:
                form.add_error(None, "Por favor, complete el captcha.")
                return render(request, 'acceso/signup.html', {'form': form})
            
            user = form.save()
            login(request, user)
            user.save()
            return redirect('seleccionar_tipo_usuario')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'acceso/signup.html', {'form': form})

# Vista para seleccionar el tipo de usuario (dueño de mascota o servicio)

def seleccionar_tipo_usuario(request):
    if request.method == 'POST':
        tipo_usuario_form = TipoUsuarioForm(request.POST)
        if tipo_usuario_form.is_valid():
            tipo_usuario = tipo_usuario_form.save(commit=False)
            tipo_usuario.usuario = request.user
            tipo_usuario.save()
            if tipo_usuario.tipo_usuario == 'dueno':
                return redirect('agregar_mascota')  # Redirige al registro de mascota
            elif tipo_usuario.tipo_usuario == 'servicios':
                return redirect('registrar_servicio')  # Redirige al crear el servicio
    else:
        tipo_usuario_form = TipoUsuarioForm()
    
    return render(request, 'acceso/tipoUsuario.html', {'tipo_usuario_form': tipo_usuario_form})

def agregar_mascota(request):
    user = request.user
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.dueno = user  # Asigna directamente el usuario actual
            mascota.save()
            return redirect('mi_mascota')
    else:
        form = MascotaForm()
        
    return render(request, 'acceso/registroMascota.html', {'form': form, 'tipo_usuario': tipo_usuario})


def cerrar_sesion(request):
    logout(request)
    return redirect('home')


