from django.urls import path
from acceso.views import inicio_sesion, registro, cerrar_sesion, agregar_mascota

urlpatterns = [
    path('login/',inicio_sesion, name='login'),
    path('registro/',registro,name='signup'),
    path('logout/',cerrar_sesion,name='logout'),
    path('agregar-mascota/',agregar_mascota,name='agregar_mascota')
]