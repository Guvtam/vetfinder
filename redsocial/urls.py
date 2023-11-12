from django.urls import path
from .views import mi_red, buscar_amigo, crear_publicacion, perfil_mascota, perfil_usuario, ver_galeria_mascota, detalle_img_mascota#, publicar_mensaje_usuario#, publicar_mensaje_mascota



urlpatterns=[
    path('mi-red/',mi_red, name='mi_red'),
    path('buscar-amigo/',buscar_amigo, name='buscar_amigo'),
    
    path('publicar/',crear_publicacion, name='crear_publicacion'),
    path('ver-perfil-usuario/<int:usuario_id>/',perfil_usuario, name='perfil_usuario'),
    path('ver-perfil-mascota/<int:mascota_id>/',perfil_mascota, name='perfil_mascota'),
    path('galeria-mascota/<int:mascota_id>/',ver_galeria_mascota, name='galeria_mascota'),
    path('galeria-mascota/img/<int:imagen_id>/',detalle_img_mascota, name='detalle_img_mascota'),
    #path('perfil-mascota/mensajes/<int:mascota_id>/',publicar_mensaje_mascota, name='publicar_mensaje_mascota'),
    #path('perfil-usuario/<int:usuario_id>/comentar/',publicar_mensaje_usuario, name='publicar_mensaje_usuario'),
   
    
    
    
    
]