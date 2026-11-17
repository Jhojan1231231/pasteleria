from django.shortcuts import render, get_object_or_404
from .models import producto, linea


def catalogo(request):

    productos = producto.objects.filter(
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

    lineas = linea.objects.all().order_by('nombre')

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
        producto,
        id=producto_id,
        disponible=True
    )

    return render(
        request,
        'pasteleria/detalle.html',
        {'producto': producto}
    )