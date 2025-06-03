from django.shortcuts import render, get_object_or_404, redirect
from .models import Videojuego
from .forms import VideojuegoForm



#Create
def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'videojuegos/formulario.html', {'form': form})

#Read
def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    context = {
        'videojuegos': videojuegos
    } 
    return render(request, 'videojuegos/lista.html', context)

#Detail
def detalle_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)
    return render(request, 'videojuegos/detalle.html', {'videojuego': videojuego})
#Update
def editar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)

    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'videojuegos/formulario.html', {'form': form})

#Delete
def eliminar_videojuego(request, pk):
    videojuego = get_object_or_404(Videojuego, pk=pk)

    if request.method == 'POST':
        videojuego.delete()
        return redirect('lista_videojuegos')
    return render(request, 'videojuegos/confirmar_eliminar.html', {'videojuego': videojuego})