from django.contrib import admin
from .models import Categoria,Post

# Register your models here.
#Construimos el panel de administracion de blog

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')#caompos de solo lectura

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)