from dataclasses import field
from django.contrib import admin

from vehiculo.models import Arreglo, Vehiculo


class VehiculoAdmin(admin.ModelAdmin):
    pass


class ArregloAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Arreglo, ArregloAdmin)
