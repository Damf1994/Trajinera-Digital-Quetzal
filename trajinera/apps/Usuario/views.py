from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.Menu.models import Alimento
from apps.Usuario.forms import AlimentoForm

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





