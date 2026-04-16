from django.urls import path
from . import views

app_name = 'solicitudes'

urlpatterns = [
    path('', views.crear_solicitud, name='crear'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
