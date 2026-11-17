from django.contrib import admin
from django.utils.html import format_html
from .models import Linea, Producto, Encargo

# Administracion en linea

@admin.register(Linea)
class LineaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('nombre',)
    

# Administracion de productos

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'mostrar_imagen',
        'nombre',
        'linea',
        'mostrar_precio',
        'porciones',
        'apto_celiacos',
        'stock',
        'disponible'
    )

    list_filter = ('linea', 'apto_celiacos')
    search_fields = ('nombre',)

    @admin.display(description='Fotografía')
    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="70" height="60" style="object-fit: cover; border-radius: 8px;" />',
                obj.imagen.url
            )
        return 'Sin imagen'

    @admin.display(description='Precio')
    def mostrar_precio(self, obj):
        return f"${obj.precio:,.0f}".replace(",", ".")
    
    
# Administracion de encargos

@admin.register(Encargo)
class EncargoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre_cliente', 'producto', 'fecha_retiro',)
    
    list_filter = ('fecha_retiro', 'producto')
    
    search_fields = ('nombre_cliente', 'correo') 