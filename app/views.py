from django.shortcuts import render, redirect
from app.forms2 import ProdutosForm, EmpresasForm
from app.models import Produtos

# Create your views here.

def home(request):
    data = {}
    data['db'] = Produtos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['forms'] = ProdutosForm()
    return render(request, 'forms.html', data)

def form_empresas(request):
    data = {}
    data['forms_empresas'] = EmpresasForm()
    return render(request, 'forms_empresa.html', data)

def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def create_empresas(request):
    forms_empresas = EmpresasForm(request.POST or None)
    if forms_empresas.is_valid():
        forms_empresas.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['forms'] = ProdutosForm(instance=data['db'])
    return render(request, 'forms.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get( pk=pk )
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return  redirect('home')