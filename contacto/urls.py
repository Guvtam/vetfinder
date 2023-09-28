from django.urls import path
from contacto.views import contacto

urlpatterns=[
    path('contacto/',contacto, name='contacto')
]