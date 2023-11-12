from django.shortcuts import render, redirect
from .forms import ContactoForm
from acceso.views import TipoUsuario

def contacto(request):
    tipo_usuario = None

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto')
    else:
        # Si el usuario ha iniciado sesión, prellenar automáticamente los campos de correo y nombre
        if request.user.is_authenticated:
            form = ContactoForm(initial={'correo': request.user.email, 'nombre': request.user.get_full_name()})
        else:
            form = ContactoForm()

    return render(request, 'contacto/contacto.html', {'tipo_usuario': tipo_usuario, 'form': form})
