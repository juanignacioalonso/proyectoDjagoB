from django.shortcuts import render, HttpResponse

from carro.carro import Carro



# Create your views here.

def home(request):
    miCarro=Carro(request) #Esto es para siempre tener iniciado un carro pq si no el context_processor de el carro cuado cerramos la secion y la volvemos a abrir da error pq no tiene un carro iniciado
    return render(request,'ProyectoWebApp/home.html')




