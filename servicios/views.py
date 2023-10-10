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
            return redirect('home')
    else:
        form = ServicioForm()

    return render(request, 'servicios/registroServicio.html', {'form': form, 'user': user, 'tipo_usuario': tipo_usuario})


def ver_servicio(request):
    servicios = Servicio.objects.all()
    form = BusquedaForm()  
    return render(request, 'servicios/servicios.html', {'servicios': servicios, 'form': form})


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

class BuscarServiciosView(ListView):
    model = Servicio
    template_name = 'servicios/servicios.html'
    context_object_name = 'servicios'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Servicio.objects.filter(nombre__icontains=query)
        else:
            return Servicio.objects.all()
        






