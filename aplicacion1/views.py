from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion1/home.html")

def juego(request):
    contexto = {'juegos': juegos.objects.all() }
    return render(request, 'aplicacion1/juegos.html', contexto)

def vendedor(request):
    contexto = {'vendedores': vendedores.objects.all() }
    return render(request, "aplicacion1/vendedores.html", contexto)

def usuario(request):
    contexto = {'usuarios': usuarios.objects.all() }
    return render(request, "aplicacion1/usuarios.html", contexto)

def comentario(request):
    contexto = {'comentarios': comentarios.objects.all() }
    return render(request, "aplicacion1/comentarios.html", contexto)

def figura(request):
    contexto = {'figuras': figuras.objects.all() }
    return render(request, "aplicacion1/figuras.html", contexto)

def usuariosForm(request):
    if request.method == "POST":
        Formulario= LoginForm(request.POST)
        if  Formulario.is_valid():
            usuario_nombre= Formulario.cleaned_data.get("nombre")
            usuario_apellido= Formulario.cleaned_data.get("apellido")
            usuario_email= Formulario.cleaned_data.get("mail")
            
            Usuario = usuarios(nombre=usuario_nombre, apellido=usuario_apellido, email=usuario_email)
            Usuario.save()
            return render(request, "aplicacion1/home.html")
    else:
        Formulario= LoginForm()
    
    return render(request, "aplicacion1/formularioUsuarios.html", {"form":Formulario})

def juegosForm(request):
    if request.method == "POST":
        Formulario= JuegosForm(request.POST)
        if  Formulario.is_valid():
            juego_nombre= Formulario.cleaned_data.get("nombre")
            juego_genero= Formulario.cleaned_data.get("genero")
            juego_clasificacion= Formulario.cleaned_data.get("clasificacion")
            juego_precio= Formulario.cleaned_data.get("precio")
            
            Juego = juegos(nombre=juego_nombre, genero=juego_genero, clasificacion=juego_clasificacion, precio=juego_precio)
            Juego.save()
            return render(request, "aplicacion1/home.html")
    else:
        Formulario= JuegosForm()
    
    return render(request, "aplicacion1/formularioJuegos.html", {"form":Formulario})

def figurasForm(request):
    if request.method == "POST":
        Formulario= FigurasForm(request.POST)
        if  Formulario.is_valid():
            figura_nombre= Formulario.cleaned_data.get("nombre")
            figura_saga= Formulario.cleaned_data.get("saga")
            figura_precio= Formulario.cleaned_data.get("precio")
            
            Figura = figuras(nombre=figura_nombre, saga=figura_saga, precio=figura_precio)
            Figura.save()
            return render(request, "aplicacion1/home.html")
    else:
        Formulario= FigurasForm()
    
    return render(request, "aplicacion1/formularioFiguras.html", {"form":Formulario})

def comentarioForm(request):
    if request.method == "POST":
        Formulario= ComentarioForm(request.POST)
        if  Formulario.is_valid():
            Comentarios_= Formulario.cleaned_data.get("comentario") 
            Comentarios = comentarios(comentario=Comentarios_)
            Comentarios.save()
            return render(request, "aplicacion1/home.html")
    else:
        Formulario= ComentarioForm()
    
    return render(request, "aplicacion1/formularioComentario.html", {"form":Formulario})

def buscar(request):
    return render(request, "aplicacion1/buscar.html")

def buscarJuegos(request):
    if request.GET["buscar"]:
        patronB= request.GET["buscar"]
        Juego = juegos.objects.filter(nombre__icontains=patronB)
        contexto = {'juegos':Juego}
        return render(request, "aplicacion1/juegos.html", contexto)
    return HttpResponse("No se encontró los datos solicitados")