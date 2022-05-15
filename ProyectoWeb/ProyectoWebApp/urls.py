from django.urls import path

from ProyectoWebApp import views

#Esto es para organizar las url si tenemos muchas aplicaciones dentro del proyecto

urlpatterns = [
    # El admin solo queda en el proyecto
    path('',views.home,name='Home'),
    path('servicios',views.servicios,name='Servicios'),
    path('tienda',views.tienda,name='Tienda'),
    path('blog',views.blog,name='Blog'),
    path('contacto',views.contacto,name='Contacto'),
    
]
