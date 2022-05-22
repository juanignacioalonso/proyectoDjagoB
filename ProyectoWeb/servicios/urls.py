from django.urls import path

from . import views #viene de del views de servicios por eso el punto

from django.conf import settings 

from django.conf.urls.static import static 



urlpatterns = [
    
    path('',views.servicios,name='Servicios'),
    
    
]

