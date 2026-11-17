from django import forms
from django.utils import timezone
from .models import Encargo


class EncargoForm(forms.ModelForm):

    class Meta:
        model = Encargo

        fields = [
            'nombre_cliente',
            'correo',
            'fecha_retiro',
            'cantidad'
        ]

        widgets = {
            'nombre_cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre'
            }),

            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),

            'fecha_retiro': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 3
            }),
        }

    def __init__(self, *args, producto=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.producto = producto

    def clean_fecha_retiro(self):
        fecha = self.cleaned_data['fecha_retiro']

        if fecha < timezone.localdate():
            raise forms.ValidationError(
                'La fecha de retiro no puede ser anterior a hoy.'
            )

        return fecha

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']

        if cantidad < 1 or cantidad > 3:
            raise forms.ValidationError(
                'La cantidad debe estar entre 1 y 3 unidades.'
            )

        if self.producto and cantidad > self.producto.stock:
            raise forms.ValidationError(
                f'Solo quedan {self.producto.stock} unidades disponibles.'
            )

        return cantidad