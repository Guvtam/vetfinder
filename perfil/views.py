from django.shortcuts import render, redirect
from acceso.models import Mascota, TipoUsuario
from acceso.forms import MascotaForm

# Create your views here.
def mi_perfil(request):
    user = request.user
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    return render(request, 'perfil/mi_perfil.html', {'user': user, 'tipo_usuario': tipo_usuario})

def mi_mascota(request):
    user = request.user
    mascota = Mascota.objects.filter(dueno=user).first()
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None
    if mascota:
        return render(request, 'perfil/mascota.html', {'mascota': mascota,'user': user, 'tipo_usuario': tipo_usuario})
    else:
        return redirect('agregar_mascota')
   
def mis_servicios(request):
    user = request.user
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    return render(request, 'perfil/mis_servicios.html', {'user': user, 'tipo_usuario': tipo_usuario})
    