from email import message
import django
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    #Muestra el formulario registro
    def get(self,request):
        form= UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})
    #Envio de informacion a la BD
    def post(self,request):
        form= UserCreationForm(request.POST)#Esta instrucción guardara la información en la BD
        if form.is_valid():

            usuario=form.save()#variable donde guardamos la información del formulario
            login(request,usuario)#Loguear el usuario
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])

            return render(request,"registro/registro.html",{"form":form})

def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

            

