from django.urls import path
from .views import home, pagina_no_encontrada
from django.conf.urls import handler404

urlpatterns = [
    path('',home, name='home')
]

handler404 = 'home.views.pagina_no_encontrada'