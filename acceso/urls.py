from django.urls import path
from acceso.views import inicio_sesion, registro_dueno_mascota, cerrar_sesion, agregar_mascota, seleccionar_tipo_usuario, cancelar


urlpatterns = [
    path('login/',inicio_sesion, name='login'),
    path('registro-usuario/',registro_dueno_mascota,name='signup'),
    path('logout/',cerrar_sesion,name='logout'),
    path('agregar-mascota/',agregar_mascota,name='agregar_mascota'),
    path('selecciona-usuario/',seleccionar_tipo_usuario,name='seleccionar_tipo_usuario'),
    path('cancelar/',cancelar,name='cancelar')
    
]