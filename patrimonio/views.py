from django.shortcuts import get_object_or_404, redirect, render

from patrimonio.forms import PatrimonioForm
from patrimonio.models import Patrimonio
from patrimonio.forms import EmprestimoForm
from patrimonio.models import Emprestimo
from patrimonio.forms import InventarioForm
from patrimonio.models import Inventario

# Create your views here.

def criar_patrimonio(request):
    if request.method == 'POST':
        form = PatrimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_patrimonios')
    else:
        form = PatrimonioForm()
    return render(request, 'patrimonios/criar_patrimonio.html', {'form': form})

def listar_patrimonios(request):
    patrimonios = Patrimonio.objects.all()
    return render(request, 'patrimonios/listar_patrimonios.html', {'patrimonios': patrimonios})

def editar_patrimonio(request, id):
    patrimonio = get_object_or_404(Patrimonio, id=id)
    if request.method == 'POST':
        form = PatrimonioForm(request.POST, instance=patrimonio)
        if form.is_valid():
            form.save()
            return redirect('listar_patrimonios')
    else:
        form = PatrimonioForm(instance=patrimonio)

    return render(request, 'patrimonios/editar_patrimonio.html', {'form': form, 'patrimonio': patrimonio})

def excluir_patrimonio(request, pk):
    patrimonio = get_object_or_404(Patrimonio, pk=pk)
    patrimonio.delete()
    return redirect('listar_patrimonios')

# Emprestimos
def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimos/criar_emprestimo.html', {'form': form})

def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimos/listar_emprestimos.html', {'emprestimos': emprestimos})

def editar_emprestimo(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm(instance=emprestimo)

    return render(request, 'emprestimos/editar_emprestimo.html', {'form': form, 'emprestimo': emprestimo})

def excluir_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    emprestimo.delete()
    return redirect('listar_emprestimos')

#Inventario
def criar_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inventarios')
    else:
        form = InventarioForm()
    return render(request, 'inventarios/criar_inventario.html', {'form': form})

def listar_inventarios(request):
    inventarios = Inventario.objects.all()
    return render(request, 'inventarios/listar_inventario.html', {'inventarios': inventarios})

def editar_inventario(request, id):
    inventario = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return redirect('listar_inventarios')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'inventarios/editar_inventario.html', {'form': form, 'inventario': inventario})

def excluir_inventario(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    inventario.delete()
    return redirect('listar_inventarios')