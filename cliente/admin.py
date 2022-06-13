from django.contrib import admin

# Register your models here.

from cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellidos','email','telefono','calle')

admin.site.register(Cliente, ClienteAdmin)