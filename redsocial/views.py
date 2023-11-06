from django.shortcuts import render, redirect, get_object_or_404
from .forms import PublicacionForm, BusquedaAmigoForm, GaleriaMascotaForm, ComentarioForm, MensajeForm, ComentarioUsuarioForm
from acceso.models import DuenoMascota, Mascota
from django.contrib.auth.models import User
from django.contrib import messages
from .models import GaleriaMascota, Comentario, Mensaje, ComentarioUsuario
from acceso.models import TipoUsuario

def mi_red(request):
    tipo_usuario = None
    user_id = None  

    if request.user.is_authenticated:
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
            user_id = request.user.id  
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    formulario = PublicacionForm()
    return render(request, 'redsocial/mi_red.html', {'formulario': formulario, 'tipo_usuario': tipo_usuario, 'user_id': user_id})



def crear_publicacion(request):
    formulario = PublicacionForm()
    
    if request.method == 'POST':
        formulario = PublicacionForm(request.POST)
        if formulario.is_valid():
            nueva_publicación = formulario.save(commit=False)
            nueva_publicación.autor = request.user
            nueva_publicación.save()
            messages.success(request, 'Tu publicación se creó con éxito.')
            return redirect('mi_red')
    
    return render(request, 'redsocial/mi_red.html', {'formulario': formulario})




def buscar_amigo(request):
    form = BusquedaAmigoForm()
    resultados = None
    tipo_usuario = None  
    if request.user.is_authenticated:
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'GET':
        form = BusquedaAmigoForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            search_by = form.cleaned_data.get('search_by')  

            if search_by == 'usuario':
                resultados = DuenoMascota.objects.filter(
                    tipousuario__tipo_usuario='dueno',
                    username__icontains=query
                )
            elif search_by == 'mascota':
                resultados = Mascota.objects.filter(
                    nombre__icontains=query
                )

    return render(request, 'redsocial/buscar_amigo.html', {'form': form, 'resultados': resultados, 'tipo_usuario': tipo_usuario})




def perfil_usuario(request, usuario_id):
    usuario = get_object_or_404(DuenoMascota, id=usuario_id)
    tipo_usuario = None
    user_info = {}  # Inicializa un diccionario para la información no frágil

    if request.user.is_authenticated:
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
            user_info = {
                'username': request.user.username,
                'email': request.user.email,
                'date_joined': request.user.date_joined,
            }
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'POST':
        form = ComentarioUsuarioForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el comentario
            comentario = form.save(commit=False)
            comentario.emisor = request.user
            comentario.receptor = usuario
            comentario.save()
            # Redirigir a la misma página después de procesar el formulario
            return redirect('perfil_usuario', usuario_id=usuario_id)
    else:
        form = ComentarioUsuarioForm()
    comentarios = ComentarioUsuario.objects.filter(receptor=usuario)
    return render(request, 'redsocial/perfil_usuario.html', {
        'perfil': usuario,
        'tipo_usuario': tipo_usuario,
        'user_info': user_info,  # Pasar la información no frágil del usuario
        'form': form,
        'comentarios': comentarios
    })

def perfil_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    tipo_usuario = None 
    if request.user.is_authenticated:
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    return render(request, 'redsocial/perfil_mascota.html', {'perfil': mascota, 'tipo_usuario': tipo_usuario})





def ver_galeria_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    form = GaleriaMascotaForm()
    es_dueno = request.user == mascota.dueno
    tipo_usuario = None  
    if request.user.is_authenticated:
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'POST' and 'imagen' in request.POST and es_dueno:
        form = GaleriaMascotaForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_imagen = form.save(commit=False)
            nueva_imagen.mascota = mascota
            nueva_imagen.autor = request.user
            nueva_imagen.save()
            return redirect('galeria_mascota', mascota_id=mascota_id)

    galeria = GaleriaMascota.objects.filter(mascota=mascota)
    
    return render(request, 'redsocial/galeria.html', {'mascota': mascota, 'galeria': galeria, 'form': form, 'es_dueno': es_dueno, 'tipo_usuario': tipo_usuario})

def detalle_img_mascota(request, imagen_id):
    imagen = get_object_or_404(GaleriaMascota, id=imagen_id)
    form = ComentarioForm()
    comentarios = Comentario.objects.filter(imagen=imagen)
    tipo_usuario = None  
    if request.user.is_authenticated:
        try:
            tipo_usuario_obj = TipoUsuario.objects.get(usuario=request.user)
            tipo_usuario = tipo_usuario_obj.tipo_usuario
        except TipoUsuario.DoesNotExist:
            tipo_usuario = None

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.autor = request.user
            nuevo_comentario.imagen = imagen
            nuevo_comentario.save()
            return redirect('detalle_img_mascota', imagen_id=imagen_id)

    return render(request, 'redsocial/detalle_foto.html', {'imagen': imagen, 'comentarios': comentarios, 'form': form, 'tipo_usuario': tipo_usuario})



def publicar_mensaje_mascota(request, mascota_id):
    receptor = Mascota.objects.get(id=mascota_id)  
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo_mensaje = form.save(commit=False)
            nuevo_mensaje.emisor = request.user
            nuevo_mensaje.receptor = receptor  
            nuevo_mensaje.save()
            return redirect('publicar_mensaje', mascota_id=mascota_id) 
    else:
        form = MensajeForm()

    mensajes = Mensaje.objects.filter(receptor=receptor) 
    return render(request, 'redsocial/mensaje.html', {'form': form, 'mensajes': mensajes, 'mascota_id': mascota_id})

'''def publicar_mensaje_usuario(request, receptor_id):
    receptor = get_object_or_404(DuenoMascota, id=receptor_id)

    if request.method == 'POST':
        form = ComentarioUsuarioForm(request.POST, instance=ComentarioUsuario(emisor=request.user, receptor=receptor))
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario', usuario_id=receptor_id)

    else:
        form = ComentarioUsuarioForm()

    return render(request, 'redsocial/perfil_usuario.html', {'form': form, 'receptor': receptor})'''