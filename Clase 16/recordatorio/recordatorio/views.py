from django.shortcuts import render, redirect, reverse

def vistaNotas(request):
    return render(
        request,
        'notas/index.html'
    )