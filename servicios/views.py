from django.shortcuts import get_object_or_404, render, redirect
from .models import Servicio

def ver_servicio(request):
    servicios = Servicio.objects.all()
    return render(request,'servicios/servicios.html',{'servicios':servicios})

def detalle_servicio(request,id):
    servicio = get_object_or_404(Servicio, pk=id)
    return render(request, 'servicios/detalle_servicio.html', {'servicio': servicio})