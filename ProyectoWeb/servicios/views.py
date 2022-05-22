from django.shortcuts import render

from servicios.models import Servicio #Hacemos referencia en este caso al models de servicio

# Create your views here.

def servicios(request):
    
    servicios=Servicio.objects.all()#Importamos todos los objetos creados en la clase Servicio
    return render(request,'servicios/servicios.html',{"servicios" : servicios})# apuntamos a la carpeta que esta en templates de la app servicios

