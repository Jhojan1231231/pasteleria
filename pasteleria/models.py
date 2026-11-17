from django.db import models
import uuid


class Linea(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    
    porciones = models.PositiveIntegerField()
    
    apto_celiacos = models.BooleanField(default=False)
    
    stock = models.PositiveIntegerField(default=0)
    
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    

class Encargo(models.Model):
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='encargos')
    nombre_cliente = models.CharField(max_length=100)
    
    correo = models.EmailField()
    
    fecha_retiro = models.DateField()
    
    fecha_encargo = models.DateField(auto_now_add=True)
    
    cantidad = models.PositiveIntegerField()
    
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre_cliente}" 
