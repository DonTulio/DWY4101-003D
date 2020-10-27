from django import forms
from .models import Publicacion

class FormPublicaciones(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = (
            'titulo',
            'detalle',
            'imagen'
        )