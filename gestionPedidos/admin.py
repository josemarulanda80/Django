from django.contrib import admin
from gestionPedidos.models import Clientes,Articulos,Pedidos
# Register your models here.
#Coloco los modelos creados en models
class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre','dirreccion','tfno')
    search_fields=('nombre','tfno')
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)
class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Pedidos,PedidosAdmin)
admin.site.register(Articulos,ArticulosAdmin)