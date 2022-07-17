class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        
        self.carro=carro

    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,

            }
        else:
            for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio 
                    break #esto es para que pare cuando encuentra el producto sale del bucle y no sigue recorriendo
        self.guardarCarro()

    def guardarCarro(self):
        self.session["carro"]=self.carro
        self.session.modified=True #funcion para modificar

    def eliminar(self,producto): #Para eliminar un producto completo
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardarCarro()

    def restarProducto(self,producto):
        for key,value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-producto.precio 
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break 
        self.guardarCarro()

    def limpiarCarro(self,producto):
        carro=self.session["carro"]={}
        self.session.modified=True