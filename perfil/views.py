from django.shortcuts import render

# Create your views here.
def mi_perfil(request):
    return render(request,'perfil/mi_perfil.html')

def mi_mascota(request):
    return render(request,'perfil/mascota.html')