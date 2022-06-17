from .carro import Carro

# Creacion de la variable global

def importe_total_carro(request):
    total=0
    miCarro=Carro(request)
    if request.user.is_authenticated:
        for value in request.session["carro"].items():
            total=total+(float(value["precio"])*value["cantidad"])
    return {"importe_total_carro":total}
