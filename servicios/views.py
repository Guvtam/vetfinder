from django.shortcuts import get_object_or_404, render, redirect
from .models import Servicio, Calificacion
from .forms import BusquedaForm, CalificacionForm, ServicioForm
from django.views.generic import ListView
from django.db.models import Q
from acceso.models import TipoUsuario


def registrar_servicio(request):
    user = request.user
    tipo_usuario = None

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.usuario = user  # Asigna el usuario directamente
            servicio.save()
            return redirect('mis_servicios')
    else:
        form = ServicioForm()

    return render(request, 'servicios/registroServicio.html', {'form': form, 'user': user, 'tipo_usuario': tipo_usuario})


def ver_servicio(request):
    servicios = Servicio.objects.all()
    form = BusquedaForm()
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
    return render(request, 'servicios/servicios.html', {'servicios': servicios, 'form': form, 'tipo_usuario': tipo_usuario})


def detalle_servicio(request,id):
    servicio = get_object_or_404(Servicio, pk=id)
    calificaciones = Calificacion.objects.filter(servicio=servicio)
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            nueva_calificacion = form.save(commit=False)
            nueva_calificacion.servicio = servicio
            nueva_calificacion.usuario = request.user  
            nueva_calificacion.save()
            return redirect('detalle_servicio', id=id)
    else:
        form = CalificacionForm()
    return render(request, 'servicios/detalle_servicio.html', {'servicio': servicio, 'calificaciones': calificaciones, 'form': form})

      



def buscar_servicio(request):
    servicios = Servicio.objects.all()
    form = BusquedaForm(request.GET)
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        categoria = form.cleaned_data.get('categoria')
        calificacion = form.cleaned_data.get('calificacion')
        
        if query:
            servicios = servicios.filter(nombre__icontains=query)
        
        if categoria:
            servicios = servicios.filter(categoria=categoria)
        
        if calificacion:
            calificacion_int = int(calificacion)
            servicios = servicios.filter(calificacion__calificacion=calificacion_int)
        
        # Limpiar los parámetros de la URL de consulta
        request.GET = request.GET.copy()
        request.GET.clear()
    
    return render(request, 'servicios/servicios.html', {'servicios': servicios, 'form': form})




def mapas(request):
    return render(request,'servicios/mapas.html')