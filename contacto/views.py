from django.shortcuts import render
from acceso.views import TipoUsuario


# Create your views here.
def contacto(request):
    user = request.user
    tipo_usuario = None  # Inicializa tipo_usuario como None por defecto

    # Verifica si el usuario está autenticado y si tiene un TipoUsuario asociado
    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    return render(request, 'contacto/contacto.html', {'tipo_usuario': tipo_usuario})
