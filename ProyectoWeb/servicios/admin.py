from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin): #Clse para leer los campos created y updated
    readonly_fields=('created','updated')

admin.site.register(Servicio,ServicioAdmin)#Registramos en el admin la clase sevisio que es el modelado de la base
