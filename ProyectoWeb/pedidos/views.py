from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ProyectoWeb.pedidos.models import LineaPedido
from carro.carro import Carro
from django.contrib import messages

from pedidos.models import Pedido

# Create your views here.
@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value("cantidad"),
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)#El metodo bulk_create es cosi hiciera muchas instrucciones de inser into procesadas en lotes en este caso los tenemos como en una lista
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.username,
        emailusuario=request.usermail
    )
    messages.seccess(request,"El pedido se ha creado correctamente")
    return redirect("../tienda")

