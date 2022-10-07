from django.shortcuts import render
from django.http import HttpResponse
import requests


def principal(request):
    return render(request,"index.html")

def listaEmpresas(request):
    response= requests.get('http://localhost:8000/aplicacion/Empresa/')
    Empr=response.json()
    print(Empr)
    return render (request,"Empresas.html",Empr)

def listaEmpleado(request):
    response= requests.get('http://localhost:8000/aplicacion/Empleado/')
    Empl=response.json()
    print(Empl)
    return render (request,"Empleado.html",Empl)