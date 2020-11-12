from rest_framework import serializers
from .models import Nota

class NotaSerialize(serializers.ModelSerializer):

    class Meta:
        model = Nota
        fields = (
            'titulo',
            'detalle',
            'creacion',
            'activa',
            'id'
        )