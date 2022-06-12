from django.shortcuts import render

from .carro import Carro

from tienda.models import Producto

from django.shortcuts import redirect #cuando redireccionemos al eliminar o modificar los productos 
# Create your views here.

def agregarProducto(request,producto_id):
    carro=Carro(request)#Creamos el carro
    producto=Producto.objects.get(id=producto_id)#obtenemos el producto
    carro.agregar(producto=producto) #Agregamos el producto al carro
    return redirect("tienda")

def eliminarProducto(request,producto_id):
    carro=Carro(request)#Creamos el carro
    producto=Producto.objects.get(id=producto_id)#obtenemos el producto
    carro.eliminar(producto=producto) #Eliminamos el producto al carro
    return redirect("tienda")

def restarProducto(request,producto_id):
    carro=Carro(request)#Creamos el carro
    producto=Producto.objects.get(id=producto_id)#obtenemos el producto
    carro.restarProducto(producto=producto) #Restamos el producto al carro
    return redirect("tienda")

def LimpiarCarro(request,producto_id):
    carro=Carro(request)#Creamos el carro
    carro.limpiarCarro()
    return redirect("tienda")
