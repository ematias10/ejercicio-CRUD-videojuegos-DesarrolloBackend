from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_videojuegos, name='lista_videojuegos'),
    path('<int:pk>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('<int:pk>/eliminar/', views.eliminar_videojuego, name='eliminar_videojuego'),
    path('<int:pk>/editar/', views.editar_videojuego, name='editar_videojuego'),
    path('crear/', views.crear_videojuego, name='crear_videojuego'),
]