from django.urls import path
from servicios.views import ver_servicio,detalle_servicio

urlpatterns=[
    path('servicios/',ver_servicio,name='servicios'),
    path('servicio/<int:id>/',detalle_servicio,name='detalle_servicio')
]