from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('juegos/', juego, name="juegos" ),
    path('vendedores/', vendedor, name="vendedores" ),
    path('usuarios/', usuario, name="usuarios" ),
    path('comentarios/', comentario, name="comentarios" ),
    path('figuras/', figura, name="figuras" ),
    
    
    #Formularios
    path('formularioUsuarios/', usuariosForm, name="formularioUsuarios"),
    path('formularioJuegos/', juegosForm, name="formularioJuegos"),
    path('formularioFiguras/', figurasForm, name="formularioFiguras"),
    path('formularioComentario/', comentarioForm, name="formularioComentario"),
    
    #Busqueda
    path('buscar/', buscar, name="buscar"),
    path('buscarJuego/', buscarJuegos, name="buscarJuego"),        
  
]
