from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Videojuego, Plataforma, Genero, Alquiler
from .forms import VideojuegoForm, AlquilerForm
import datetime

def tempplatgen(request):
    plataformas = Plataforma.objects.all()
    generos = Genero.objects.all()
    return render(request, 'genero-plataforma.html', {'plataformas': plataformas, 'generos': generos})

def registrar_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = VideojuegoForm()
    return render(request, 'juegos.html', {'form': form})

def registrar_alquiler(request):
    cliente = request.POST['cliente']
    videojuego_id = request.POST['juego']
    fecha_alquiler = datetime.datetime.now()
    
    videojuego = Videojuego.objects.get(id=videojuego_id)
    videojuego.stock -= 1
    videojuego.save()
    
    alquiler = Alquiler.objects.create(cliente=cliente, videojuego=videojuego, fecha_alquiler=fecha_alquiler)
    
    return redirect('lista_alquileres')
         
def finalizar_alquiler(request, pk):
    print(f"PK recibido: {pk}")  # Esto imprimirá el pk en la consola
    alquiler = get_object_or_404(Alquiler, pk=pk)
    
    alquiler.fecha_devolucion = timezone.now()
    alquiler.save()
        
    videojuego = alquiler.videojuego
    videojuego.stock += 1
    videojuego.save()
        
    return redirect('lista_alquileres')  

def todoslosjuegos(request):
    videojuegos = Videojuego.objects.all()
    plataformas = Plataforma.objects.all()
    generos = Genero.objects.all()
    if request.GET.get('plataforma'):
        videojuegos = videojuegos.filter(plataforma__id=request.GET.get('plataforma'))
    if request.GET.get('generosel'):
        videojuegos = videojuegos.filter(genero__id=request.GET.get('generosel'))
    
    return render(request, 'juegos.html', {'videojuegos': videojuegos, 'plataformas': plataformas, 'generos': generos})

def lista_alquileres(request):
    alquileres = Alquiler.objects.all()
    plataformas = Plataforma.objects.all()
    videojuegos = Videojuego.objects.all()
    return render(request, 'alquiler.html', {'alquileres': alquileres, 'plataformas': plataformas, 'videojuegos': videojuegos})

