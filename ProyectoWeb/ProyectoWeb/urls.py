"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    # De esta manera incluimos la urls de ProyectoWebApp
    path('', include('ProyectoWebApp.urls')), #Si dejamos vacio el primer argumento no tenemos que poner el la direccion la aplicacion a la que nos referimos, si tenemos mas de una hay q definirlo
    # icluimos la url servicios
    path('servicios', include('servicios.urls')),
    #Incluimos la url blog
    path('blog', include('blog.urls')),
    #Incluimos la url Contacto
    path('contacto', include('contacto.urls')),
    #Incluimos la url Tienda
    path('tienda', include('tienda.urls')),
    #Incluimos la url Carro
    path('carro', include('carro.urls')),
    #Incluimos la url Autenticacion
    path('autenticacion', include('autenticacion.urls')),

]
