from django.urls import path

from . import views


#Esto es para organizar las url si tenemos muchas aplicaciones dentro del proyecto

urlpatterns = [
    # El admin solo queda en el proyecto
    path('',views.tienda,name='Tienda'),
    
]
