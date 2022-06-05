from django.shortcuts import render
from .import views
# Create your views here.


def tienda(request):
    
    return render(request,'tienda/tienda.html')
