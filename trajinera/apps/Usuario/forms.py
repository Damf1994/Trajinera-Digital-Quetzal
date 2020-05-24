from django import forms
from apps.Menu.models import * 
from apps.Usuario.models import * 


class AlimentoForm(forms.ModelForm):

	class Meta:

		model = Alimento 

		fields = [
			'nombre',
			'precio',
			'descripcion',
			'categoria',
			'foto',
		]

		labels = {
			'nombre': 'Nombre' ,
			'precio': 'Precio' ,
			'descripcion': 'Descripcion' ,
			'categoria': 'Categoria' ,
			'foto': 'Foto' ,
		}

		widgets = {
			'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
			'precio': forms.NumberInput(),
			'descripcion': forms.TextInput(attrs = {'class': 'form-control'}),
			
		}



class CategoriaForm(forms.ModelForm):

	class Meta:

		model = Categoria

		fields = [
			'nombre',
		]

		labels = {
			'nombre': 'Nombre',
		}

		widgets = {
			'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
		}


