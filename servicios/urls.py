from django.urls import path
from servicios.views import ver_servicio,detalle_servicio, buscar_servicio, registrar_servicio, mapas

urlpatterns=[
    path('servicios/',ver_servicio,name='servicios'),
    path('servicio/<int:id>/',detalle_servicio,name='detalle_servicio'),
    path('buscar-servicio/', buscar_servicio,name='buscar_servicio'),
    path('registro-servicio/',registrar_servicio,name='registrar_servicio'),
    path('mapas/',mapas,name='mapas'),
    path('buscar-mapas/',mapas,name='buscar_mapas')
]