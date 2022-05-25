from django.shortcuts import render
from usuariossflia.models import Familiares
import datetime
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "index.html")

def lista_familiares(request):
    familiares = Familiares.objects.all()
    datos = {"datos": familiares}

    return render(request, "lista_familiares.html", datos ) 

def alta_familiares(request):
    familiar = Familiares(nombre="Pepe", edad=23, reg_alta=datetime.datetime(2022,3,12))
    familiar.save()
    familiar = Familiares(nombre="Josesito", edad=28, reg_alta=datetime.datetime(2021,10,1))
    familiar.save()
    familiar = Familiares(nombre="Ayumi", edad=33, reg_alta=datetime.datetime(2020,6,14))
    familiar.save()

    return HttpResponse("Se ejecuto correctamente")

