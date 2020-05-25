from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.Menu.models import Alimento, Categoria 
from apps.Usuario.forms import AlimentoForm, CategoriaForm

# Create your views here.

def indexAdministrador(request):
	return render(request,'admin/index_admin.html')



class menu_Alimentos_Administrador(ListView):
	model = Alimento
	template_name = 'admin/alimento/alimento.html'

class menu_Alimentos_Editar(ListView):
	model = Alimento
	template_name = 'admin/alimento/menu_editar_alimento.html'

class menu_Alimentos_Eliminar(ListView):
	model = Alimento
	template_name = 'admin/alimento/menu_eliminar_alimento.html'


class Crear_Alimento(CreateView):
	model = Alimento
	form_class = AlimentoForm
	template_name = 'admin/alimento/crear_alimento.html'
	success_url = reverse_lazy('menu_alimentos')

class Editar_Alimento(UpdateView):
	model = Alimento
	form_class = AlimentoForm
	template_name = 'admin/alimento/editar_alimento.html'
	success_url = reverse_lazy('menu_alimentos')

class Eliminar_Alimento(DeleteView):
	model = Alimento
	form_class = AlimentoForm
	template_name = 'admin/alimento/eliminar_alimento.html'
	success_url = reverse_lazy('menu_alimentos')




class menu_Categoria(ListView):
	model = Categoria
	template_name = 'admin/categoria/categorias.html'


def menu_Categoria_Alimentos(request, categoria):
	alimento = Alimento.objects.all()
	contexto = {'alimentos': alimento, 'Categoria': categoria }
	return render(request, 'admin/categoria/alimentos_categoria.html', contexto) 


class menu_Editar_Categoria(ListView):
	model = Categoria
	template_name = 'admin/categoria/menu_editar_categoria.html'

class menu_Eliminar_Categoria(ListView):
	model = Categoria
	template_name = 'admin/categoria/menu_eliminar_categoria.html'


class Crear_Categoria(CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'admin/categoria/crear_categoria.html'
	success_url = reverse_lazy('listado_categorias')

class Editar_Categoria(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'admin/categoria/editar_categoria.html'
	success_url = reverse_lazy('listado_categorias')

class Eliminar_Categoria(DeleteView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'admin/categoria/eliminar_categoria.html'
	success_url = reverse_lazy('listado_categorias')









