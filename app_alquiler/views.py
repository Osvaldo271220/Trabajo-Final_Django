from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Videojuego, Plataforma, Genero, Alquiler
from .forms import VideojuegoForm, AlquilerForm

def tempplatgen(request):
    plataformas = Plataforma.objects.all()
    generos = Genero.objects.all()
    return render(request, 'genero-plataforma.html', {'plataformas': plataformas, 'generos': generos})

def registrar_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'juegos.html', {'form': form})

def registrar_alquiler(request):
    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid():
            alquiler = form.save(commit=False)
            videojuego = alquiler.videojuego
            if videojuego.stock > 0:
                videojuego.stock -= 1
                videojuego.save()
                alquiler.save()
                return redirect('lista_alquileres')
            else:
                form.add_error('videojuego', 'No hay stock disponible para este videojuego.')
    else:
        form = AlquilerForm()
    return render(request, 'app_alquiler/registrar_alquiler.html', {'form': form})

def consultar_videojuegos(request):
    plataforma_id = request.GET.get('plataforma')
    genero_id = request.GET.get('genero')
    
    videojuegos = Videojuego.objects.all()
    
    if plataforma_id:
        videojuegos = videojuegos.filter(plataforma_id=plataforma_id)
    elif genero_id:
        videojuegos = videojuegos.filter(genero_id=genero_id)
    
    plataformas = Plataforma.objects.all()
    generos = Genero.objects.all()
    
    context = {
        'videojuegos': videojuegos,
        'plataformas': plataformas,
        'generos': generos,
    }
    
    return render(request, 'app_alquiler/consultar_videojuegos.html', context)

def finalizar_alquiler(request, alquiler_id):
    alquiler = get_object_or_404(Alquiler, id=alquiler_id)
    if request.method == 'POST':
        alquiler.fecha_devolucion = timezone.now()
        alquiler.save()
        
        videojuego = alquiler.videojuego
        videojuego.stock += 1
        videojuego.save()
        
        return redirect('lista_alquileres')
    
    return render(request, 'app_alquiler/finalizar_alquiler.html', {'alquiler': alquiler})

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    plataformas = Plataforma.objects.all()
    generos = Genero.objects.all()
    return render(request, 'juegos.html', {'videojuegos': videojuegos, 'plataformas': plataformas, 'generos': generos})

def lista_alquileres(request):
    alquileres = Alquiler.objects.all()
    plataformas = Plataforma.objects.all()
    videojuegos = Videojuego.objects.all()
    return render(request, 'alquiler.html', {'alquileres': alquileres, 'plataformas': plataformas, 'videojuegos': videojuegos})

def listar_gen_cat(request):
    plataformas = Plataforma.objects.all()
    generos = Genero.objects.all()
    return render(request, 'genero-paltaforma.html', {'plataformas': plataformas, 'generos': generos})
