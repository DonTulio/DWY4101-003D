from django.shortcuts import render
## Que necesito para usar Rest y responde json, como tambien
## entender el json que me envian
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from .serializers import NotaSerialize
from .models import Nota
# Django execptio 
from django.core.exceptions import ObjectDoesNotExist

@api_view(["GET"])
def saludar(request):
    return JsonResponse(
        {
            "mensaje":"Hola Mundo!!!"
        },
        status = status.HTTP_200_OK
    )
@api_view(["GET","POST","DELETE"])
def listarAgregarYQuizasEliminarxD(request):
    if request.method == 'POST':
        datos_traducidos = JSONParser().parse(request)
        datos_serializados = NotaSerialize(data=datos_traducidos)
        if datos_serializados.is_valid():
            datos_serializados.save()
            return JsonResponse(
                datos_serializados.data,
                status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            datos_serializados.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
    elif request.method == 'GET':
        notas = Nota.objects.all()
        notas_traducidas = NotaSerialize(notas,many=True)
        return JsonResponse(
            notas_traducidas.data,
            safe=False,
            status = status.HTTP_200_OK
        )
    elif request.method == 'DELETE':
        Nota.objects.all().delete()
        return JsonResponse(
            {
                "mensaje":"Notas borradas"
            },
            status = status.HTTP_200_OK
        )
    return JsonResponse(
        {
            "Metodo":request.method
        },
        status=status.HTTP_200_OK
    )

@api_view(["GET","PUT","DELETE"])
def buscarModificarCambiarEstado(request,uid):
    try:
        nota = Nota.objects.get(pk=uid)
    except ObjectDoesNotExist:
        return JsonResponse(
            {
                "mensaje":'nota no existe :c'
            },
            status = status.HTTP_404_NOT_FOUND
        )
    if request.method == 'GET':
        nota_traducida = NotaSerialize(nota)
        return JsonResponse(
            nota_traducida.data,
            status = status.HTTP_200_OK
        )
    return JsonResponse(
        {
            "Metodo":request.method,
            "idElemento": uid
        }
    )