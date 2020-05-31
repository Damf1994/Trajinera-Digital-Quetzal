from django.db import models
from apps.Usuario.models import Cliente, Repartidor

# Create your models here.
class Estado(models.Model):
	
	nombre = models.CharField(max_length=15)
	
	def __str__(self):
		return '{}'.format(self.nombre)

class Categoria(models.Model):
	
	nombre = models.CharField(max_length = 30)

	def __str__(self):
		return '{}'.format(self.nombre)

class Alimento(models.Model):

	nombre = models.CharField(max_length=30)
	precio = models.IntegerField()
	descripcion = models.TextField()
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='media/alimentos/images/')
	
	def __str__(self):
		return '{}'.format(self.nombre)



class Orden(models.Model):

	fecha_orden = models.DateField()
	estado_orden = models.ForeignKey(Estado, null=True , blank=True, on_delete=models.CASCADE)
	cliente_orden = models.ForeignKey(Cliente, null=True , blank=True, on_delete=models.CASCADE)
	repartidor_orden = models.ForeignKey(Repartidor, null=True , blank=True, on_delete=models.CASCADE)
	alimentos_orden = models.ManyToManyField(Alimento, blank=True)

	def __str__(self):
		return 'Orden numero: {}'.format(self.id)


