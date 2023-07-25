from django.shortcuts import render, redirect
from .forms import *
#from django.contrib.sessions.models import Session

# Create your views here.
def add_laboratorio(request, *args, **kwargs):
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_laboratorio')
    form = LaboratorioForm
    return render(request, "add_laboratorio.html", {'form':form})

def index(request):
    context = {}
    return render(request, "index.html", context)

def mostrar_laboratorio(request):
    context = {
        'laboratorios': Laboratorio.objects.all().order_by("nombre"),
        #'nvisitas': Session.objects.all().count()
        }
    nvisits = request.session.get('num_visits', 0) #Inicializa la variable
    request.session['num_visits'] = nvisits + 1 #Guarda la variable de session
    context['nvisitas'] = nvisits + 1 # Pasa la variable para render en el HTML
    return render(request, "mostrar_laboratorio.html", context)

def mostrar_directores(request):
    context = {
        'directores': DirectorGeneral.objects.all(),
        }
    return render(request, "mostrar_director.html", context)


def add_director(request, *args, **kwargs):
    if request.method == "POST":
        form = DirectorGeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_directores')
    form = DirectorGeneralForm
    return render(request, "add_director_ejecutivo.html", {'form':form})

def v_laboratorio_edit(request, laboratorio_id):
    context = {
        'item': Laboratorio.objects.get(id=laboratorio_id)
    }
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=context['item'])
        if form.is_valid():
            form.save()
            return redirect(mostrar_laboratorio)
    context['form'] = LaboratorioForm(instance=context['item'])
    return render(request, 'editar_laboratorio.html', context)

def v_laboratorio_delete(request, laboratorio_id):
    context = {
        'item': Laboratorio.objects.get(id=laboratorio_id)
    }
    if request.method == 'POST':
        context['item'].delete()
        return redirect(mostrar_laboratorio)
    return render(request, 'delete_laboratorio.html', context)


def v_director_edit(request, pk):
    context = {
        'item': DirectorGeneral.objects.get(id=pk)
    }
    if request.method == 'POST':
        form = DirectorGeneralForm(request.POST, instance=context['item'])
        if form.is_valid():
            form.save()
            return redirect(mostrar_directores)
    context['form'] = DirectorGeneralForm(instance=context['item'])
    return render(request, 'editar_director.html', context)

def v_director_delete(request, pk):
    context = {
        'item': DirectorGeneral.objects.get(id=pk)
    }
    if request.method == 'POST':
        context['item'].delete()
        return redirect(mostrar_directores)
    return render(request, 'delete_director.html', context)


def mostrar_productos(request):
    context = {
        'productos': Producto.objects.all(),
        }
    return render(request, "mostrar_productos.html", context)


def add_producto(request, *args, **kwargs):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')
    form = ProductoForm
    return render(request, "add_producto.html", {'form':form})

def v_producto_edit(request, pk):
    context = {
        'item': Producto.objects.get(id=pk)
    }
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=context['item'])
        if form.is_valid():
            form.save()
            return redirect(mostrar_productos)
    context['form'] = ProductoForm(instance=context['item'])
    return render(request, 'editar_producto.html', context)

def v_producto_delete(request, pk):
    context = {
        'item': Producto.objects.get(id=pk)
    }
    if request.method == 'POST':
        context['item'].delete()
        return redirect(mostrar_productos)
    return render(request, 'delete_producto.html', context)