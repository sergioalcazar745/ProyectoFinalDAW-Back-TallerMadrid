from django.contrib import admin
from facturacion.models import Gasto,Factura

# Register your models here.

class GastoAdmin(admin.ModelAdmin):
    list_display=('fecha','usuario','concepto','importe')
admin.site.register(Gasto, GastoAdmin)