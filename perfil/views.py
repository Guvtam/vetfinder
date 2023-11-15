from django.shortcuts import get_object_or_404, render, redirect
from acceso.models import Mascota, TipoUsuario
from acceso.forms import MascotaForm
from servicios.models import Servicio, Calificacion
from .forms import EditarPerfilForm, EditarServicioForm, EditarMascotaForm
from django.contrib.auth.decorators import login_required
from redsocial.models import ComentarioUsuario

# Create your views here.
@login_required
def mi_perfil(request):
    user = request.user
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto
    user_id = None
    comentarios = None

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        user_id = user.id
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
            comentarios = ComentarioUsuario.objects.filter(receptor=user)
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    return render(request, 'perfil/mi_perfil.html', {'user': user, 'tipo_usuario': tipo_usuario, 'user_id': user_id, 'comentarios': comentarios})


@login_required
def mi_mascota(request):
    user = request.user
    mascotas = Mascota.objects.filter(dueno=user)
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    return render(request, 'perfil/mascota.html', {'mascotas': mascotas, 'user': user, 'tipo_usuario': tipo_usuario})



@login_required
def mis_servicios(request):
    # Inicializa tipo_usuario como None por defecto
    tipo_usuario = None
    user_id = None

    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        user_id = request.user.id
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

    return render(request, 'perfil/mis_servicios.html', {'servicios': servicios, 'tipo_usuario': tipo_usuario, 'user_id': user_id})



@login_required
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




@login_required
def editar_mascota(request, mascota_id):
    mascota = Mascota.objects.get(id=mascota_id)

    # Obtener las instancias de Especie y Raza asociadas a la mascota
    especie_instancia = mascota.especie
    raza_instancia = mascota.raza

    if request.method == 'POST':
        form = EditarMascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('mi_mascota')
    else:
        form = EditarMascotaForm(instance=mascota, initial={'especie': especie_instancia, 'raza': raza_instancia})

    

    return render(request, 'perfil/editar_mascota.html', {'form': form, 'mascota': mascota})




@login_required
def editar_servicio(request, servicio_id):
    servicio = Servicio.objects.get(id=servicio_id)

    if request.method == 'POST':
        form = EditarServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('mis_servicios')  # Redirige a la página de detalle del servicio
    else:
        form = EditarServicioForm(instance=servicio)

    return render(request, 'perfil/editar_servicio.html', {'form': form, 'servicio': servicio})



@login_required
def ver_calificacion_servicios(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    calificaciones = Calificacion.objects.filter(servicio=servicio)

    return render(request, 'perfil/ver_calificacion_servicios.html', {'servicio': servicio, 'calificaciones': calificaciones})