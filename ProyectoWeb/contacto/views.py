from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
#En la vista podemos programar a donde enviamos la informacion por el metodo post
def contacto(request):
    formulario_contacto=FormularioContacto()#instanciamos la clase formulario
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)#así rescatamos la información de los cuadros de texto
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde app Django", 
            "El usuario con el nombre {} con la dirección de email {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["zalbak87@gmail.com"],reply_to=[email])

            try:
                email.send()

                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")



        
    return render(request,'contacto/contacto.html', {'miFormulario':formulario_contacto})#luego lo renderizamos