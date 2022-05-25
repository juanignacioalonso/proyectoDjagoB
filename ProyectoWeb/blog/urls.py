from django.urls import path
from . import views

urlpatterns = [
    # El admin solo queda en el proyecto
    path('',views.blog,name='Blog'),
   
    
]