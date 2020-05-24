from django.contrib import admin
from apps.Usuario.models import Admin, Cliente, Repartidor 

# Register your models here.
admin.site.register(Admin)
admin.site.register(Repartidor)
admin.site.register(Cliente)