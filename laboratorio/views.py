from django.shortcuts import render, redirect
from .forms import *
from django.contrib.sessions.models import Session

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
    pass

def mostrar_laboratorio(request):
    context = {
        'laboratorios': Laboratorio.objects.all(),
        'nvisitas': Session.objects.all().count()
        }
    return render(request, "mostrar_laboratorio.html", context)


def add_director(request, *args, **kwargs):
    if request.method == "POST":
        form = DirectorGeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_director')
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