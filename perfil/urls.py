from django.urls import path 
from .views import mi_perfil, mi_mascota,mis_servicios, editar_miperfil,editar_mascota,editar_servicio

urlpatterns=[
    path('mi-perfil/',mi_perfil,name='mi_perfil'),
    path('mi-mascota/',mi_mascota,name='mi_mascota'),
    path('mis-servicios/',mis_servicios,name='mis_servicios'),
    path('editar-perfil/',editar_miperfil,name='editar_perfil'),
    path('editar-mascota/',editar_mascota,name='editar_mascota'),
    path('editar-servicio/',editar_servicio,name='editar_servicio'),
]