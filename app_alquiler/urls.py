from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alquileres, name='home'),
    path('registrar-videojuego/', views.registrar_videojuego, name='registrar_videojuego'),
    #path('registrar-alquiler/', views.registrar_alquiler, name='registrar_alquiler'),
    path('todoslosjuegos/', views.todoslosjuegos, name='todos'),
    #path('finalizar-alquiler/', views.finalizar_alquiler, name='finalizar_alquiler'),
    path('lista-videojuegos/', views.lista_videojuegos, name='lista_videojuegos'),
    path('lista-alquileres/', views.lista_alquileres, name='lista_alquileres'),
    ]
