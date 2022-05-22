from django.urls import path

from ProyectoWebApp import views

from django.conf import settings #importamos MEDIA_URL y MEDIA_ROOT

from django.conf.urls.static import static # importamos la carpeta statics

#Esto es para organizar las url si tenemos muchas aplicaciones dentro del proyecto

urlpatterns = [
    # El admin solo queda en el proyecto
    path('',views.home,name='Home'),
    path('tienda/',views.tienda,name='Tienda'),
    path('blog/',views.blog,name='Blog'),
    path('contacto/',views.contacto,name='Contacto'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #agregamos static a urlpatterns