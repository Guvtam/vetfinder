from django.shortcuts import get_object_or_404, render, redirect
from .models import Servicio, Calificacion
from .forms import BusquedaForm, CalificacionForm
from django.views.generic import ListView
from django.db.models import Q

def ver_servicio(request):
    servicios = Servicio.objects.all()
    return render(request,'servicios/servicios.html',{'servicios':servicios})

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
            return Servicio.objects.filter(Q(nombre__icontains=query))
        else:
            return Servicio.objects.all()






