from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm, MascotaForm, LoginForm, TipoUsuarioForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Mascota , TipoUsuario, Especie, Raza
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required



def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Verifica el tipo de usuario
                try:
                    tipo_usuario_obj = TipoUsuario.objects.get(usuario=user)
                    tipo_usuario = tipo_usuario_obj.tipo_usuario
                except TipoUsuario.DoesNotExist:
                    tipo_usuario = None

                if tipo_usuario == 'dueno':
                    return redirect('mi_mascota')
                elif tipo_usuario == 'servicios':
                    return redirect('mis_servicios')
                else:
                    return redirect('mi_perfil')  # Redirige predeterminadamente

            else:
                messages.error(request, 'Credenciales inválidas o usuario desactivado.')
    else:
        form = LoginForm()
    return render(request, 'acceso/login.html', {'form': form})

    

    

def registro_dueno_mascota(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            captcha_response = request.POST.get('g-recaptcha-response')
            if not captcha_response:
                form.add_error(None, "Por favor, complete el captcha.")
                return render(request, 'acceso/signup.html', {'form': form})
            
            try:
                user = form.save()
                login(request, user)

                # Envía el correo electrónico de registro exitoso al correo del usuario
                subject = 'Registro Exitoso'
                message = 'Gracias por registrarte en nuestro sitio. Tu registro ha sido exitoso.'
                from_email = 'VETFINDER - gutierrez.valdes.t@gmail.com'
                recipient_list = [user.email]

                html_message = render_to_string('acceso/registro_exitoso.html')
                send_mail(subject, message, from_email, recipient_list, html_message=html_message)

                return redirect('seleccionar_tipo_usuario')
            except IntegrityError:
                form.add_error('email', "El correo electrónico ya está registrado. Por favor, use otro.")
                return render(request, 'acceso/signup.html', {'form': form})
    else:
        form = RegistroUsuarioForm()
    return render(request, 'acceso/signup.html', {'form': form})


# Vista para seleccionar el tipo de usuario (dueño de mascota o servicio)

@login_required
def seleccionar_tipo_usuario(request):
    if request.method == 'POST':
        tipo_usuario_form = TipoUsuarioForm(request.POST)
        if tipo_usuario_form.is_valid():
            tipo_usuario = tipo_usuario_form.save(commit=False)
            tipo_usuario.usuario = request.user
            tipo_usuario.save()
            if tipo_usuario.tipo_usuario == 'dueno':
                return redirect('agregar_mascota')  # Redirige al registro de mascota
            elif tipo_usuario.tipo_usuario == 'servicios':
                return redirect('registrar_servicio')  # Redirige al crear el servicio
            elif tipo_usuario.tipo_usuario == 'ambos' :
                return redirect('mi_perfil')
    else:
        tipo_usuario_form = TipoUsuarioForm()
    
    return render(request, 'acceso/tipoUsuario.html', {'tipo_usuario_form': tipo_usuario_form})


@login_required
def agregar_mascota(request):
    user = request.user
    tipo_usuario = None

    if user.is_authenticated:
        try:
            tipo_usuario = TipoUsuario.objects.get(usuario=user).tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.dueno = user
            mascota.save()
            return redirect('mi_mascota')
    else:
        form = MascotaForm()
        especies = Especie.objects.all()
        
        return render(request, 'acceso/registroMascota.html', {'form': form, 'tipo_usuario': tipo_usuario, 'especies': especies})

@login_required
def obtener_raza(request, especie_id):
    razas = Raza.objects.filter(especie_id=especie_id).values('id', 'nombre')  
    return JsonResponse(list(razas), safe=False)


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def cancelar(request):
    return redirect('mi_perfil')

