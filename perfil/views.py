from django.shortcuts import render, redirect
from acceso.models import Mascota, TipoUsuario
from acceso.forms import MascotaForm
from servicios.models import Servicio
from .forms import EditarPerfilForm

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
    # Inicializa tipo_usuario como None por defecto
    tipo_usuario = None

    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Recupera el tipo de usuario asociado al usuario actual
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

        # Recupera los servicios asociados al usuario actual
        servicios = Servicio.objects.filter(usuario=request.user)
    else:
        servicios = None  # El usuario no está autenticado, por lo que no hay servicios que mostrar

    return render(request, 'perfil/mis_servicios.html', {'servicios': servicios, 'tipo_usuario': tipo_usuario})




def editar_miperfil(request):
    user = request.user
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto
    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            # Redirigir a la página de perfil o a donde desees después de guardar los cambios.
            return redirect('mi_perfil')
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'perfil/editar_perfil.html', {'form': form, 'tipo_usuario': tipo_usuario})


def editar_mascota(request):
    return render(request,'perfil/editar_mascota.html')

def editar_servicio(request):
    return render(request,'perfil/editar_servicio.html')