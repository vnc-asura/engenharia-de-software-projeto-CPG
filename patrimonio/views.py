from django.shortcuts import get_object_or_404, redirect, render

from patrimonio.forms import PatrimonioForm
from patrimonio.models import Patrimonio

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