from django.shortcuts import render, get_object_or_404
from .models import Encargo, Producto, Linea
from .forms import EncargoForm
from django.db import transaction
from django.shortcuts import redirect

def catalogo(request):

    productos = Producto.objects.filter(
        disponible=True
    ).select_related('linea')

    busqueda = request.GET.get('q', '').strip()
    linea_id = request.GET.get('linea', '').strip()

    # Buscar productos por nombre
    if busqueda:
        productos = productos.filter(
            nombre__icontains=busqueda
        )

    # Filtrar productos por línea
    if linea_id:
        productos = productos.filter(
            linea_id=linea_id
        )

    lineas = Linea.objects.all().order_by('nombre')

    contexto = {
        'productos': productos,
        'lineas': lineas,
        'busqueda': busqueda,
        'linea_seleccionada': linea_id,
    }

    return render(
        request,
        'pasteleria/catalogo.html',
        contexto
    )


def detalle_producto(request, producto_id):
    producto = get_object_or_404(
        Producto,
        id=producto_id,
        disponible=True
    )

    if request.method == 'POST':
        formulario = EncargoForm(request.POST, producto=producto)

        if formulario.is_valid():
            with transaction.atomic():
                producto.refresh_from_db()

                cantidad = formulario.cleaned_data['cantidad']

                if cantidad > producto.stock:
                    formulario.add_error(
                        'cantidad',
                        f'Solo quedan {producto.stock} unidades disponibles.'
                    )
                else:
                    encargo = formulario.save(commit=False)
                    encargo.producto = producto
                    encargo.save()

                    producto.stock -= cantidad
                    producto.save(update_fields=['stock'])

                    return redirect(
                        'comprobante',
                        codigo=encargo.codigo
                    )
    else:
        formulario = EncargoForm(producto=producto)

    contexto = {
        'producto': producto,
        'formulario': formulario
    }

    return render(
        request,
        'pasteleria/detalle.html',
        contexto
    )
    
    

def comprobante(request, codigo):
    encargo = get_object_or_404(
        Encargo.objects.select_related('producto'),
        codigo=codigo
    )

    total = encargo.producto.precio * encargo.cantidad

    contexto = {
        'encargo': encargo,
        'total': total
    }

    return render(
        request,
        'pasteleria/comprobante.html',
        contexto
    )
    
    
