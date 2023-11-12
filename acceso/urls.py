from django.urls import path
from django.contrib.auth import views as auth_views
from acceso.views import inicio_sesion, registro_dueno_mascota, cerrar_sesion, agregar_mascota, seleccionar_tipo_usuario, cancelar, obtener_raza


urlpatterns = [
    path('login/',inicio_sesion, name='login'),
    path('registro-usuario/',registro_dueno_mascota,name='signup'),
    path('logout/',cerrar_sesion,name='logout'),
    path('agregar-mascota/',agregar_mascota,name='agregar_mascota'),
    path('selecciona-usuario/',seleccionar_tipo_usuario,name='seleccionar_tipo_usuario'),
    path('cancelar/',cancelar,name='cancelar'),
    path('recuperar-contrasena/', auth_views.PasswordResetView.as_view(template_name='acceso/recuperar_contrasena.html'), name='recuperar_contrasena'),
    path('recuperar-contrasena/hecho/', auth_views.PasswordResetDoneView.as_view(template_name='acceso/recuperar_contrasena_done.html'), name='password_reset_done'),
    path('recuperar-contrasena/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='acceso/recuperar_contrasena_confirm.html'), name='password_reset_confirm'),
    path('recuperar-contrasena/completado/', auth_views.PasswordResetCompleteView.as_view(template_name='acceso/recuperar_contrasena_complete.html'), name='password_reset_complete'),
    path('obtener-raza/<int:especie_id>/',obtener_raza, name='obtener_raza'),
    
]



