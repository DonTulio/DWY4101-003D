from django import forms
# Usamos los modelos
from .models import Producto

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','stock']

