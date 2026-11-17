from django.contrib import admin
from .models import linea, producto, encargo

# Administracion en linea

@admin.register(linea)
class LineaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('nombre',)
    

# Administracion de productos

@admin.register(producto)
class ProductoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'linea', 'mostrar_precio', 'porciones', 'apto_celiacos', 'stock', 'disponible')
    
    list_filter = ('linea', 'apto_celiacos')
    
    search_fields = ('nombre',)
    
    admin.display(description='Precio')
    def mostrar_precio(self, obj):
        return f"${obj.precio:,.0f}".replace(',', '.')
    
    
# Administracion de encargos

@admin.register(encargo)
class EncargoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre_cliente', 'producto', 'fecha_retiro',)
    
    list_filter = ('fecha_retiro', 'producto')
    
    search_fields = ('nombre_cliente', 'correo') 