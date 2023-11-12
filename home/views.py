from django.shortcuts import render
from acceso.models import TipoUsuario

# Create your views here.
def home(request):
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if request.user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=request.user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    return render(request, 'home/home.html', {'tipo_usuario': tipo_usuario})



def pagina_no_encontrada(request, exception):
    return render(request, '404.html', status=404)