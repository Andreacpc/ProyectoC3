#from django.shortcuts import render
from django.views import View
import json
from aplicacion.models import Empleado
from aplicacion.models import Empresas
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
class EmpresaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
    def get(self,request,codigo=""):
        if len(codigo)>0:
            Empr=list(Empresas.objects.filter(codigo=codigo).values())
            if len(Empr)>0:
                datos={'mensaje':Empr}
            else:
                datos={'mensaje':"No se encontró la empresa."}
        else:
            Empr=list(Empresas.objects.values())
            if len(Empr)>0:
                datos={"mensaje":Empr}
            else:
                datos={"mensaje":"No se encontraron empresas."}
        return JsonResponse(datos)

    def post(self,request):
        data=json.loads(request.body)
        Empr=Empresas(codigo=data['codigo'],nombre=data['nombre'], 
        ubicacion=data['ubicacion'],email=data['email'],nit=data['nit'],
        telefono=data['telefono'],sector_p=data['sector_p'])
        Empr.save()
        datos={"mensaje":"Empresa registrada exitosamente."}
        return JsonResponse(datos)
    
    def put(self,request,codigo):
        data=json.loads(request.body)
        Empr=list(Empresas.objects.filter(codigo=codigo).values())
        if len(Empr)>0:
            Empr=Empresas.objects.get(codigo=codigo)
            Empr.nombre=data["nombre"]
            Empr.ubicacion=data["ubicacion"]
            Empr.email=data["email"]
            Empr.nit=data["nit"]
            Empr.telefono=data["telefono"]
            Empr.sector_p=data["sector_p"]
            Empr.save()
            mensaje={"mensaje":"Empresa actualizada exitosamente"}
        else:
            mensaje={"mensaje":"No se encontró la empresa."}
        return JsonResponse(mensaje)

    def delete(self,request,codigo):
        Emp=list(Empresas.objects.filter(codigo=codigo).values())
        if len(Emp)>0:
            Empresas.objects.filter(codigo=codigo).delete()
            mensaje={"mensaje":"Empresa elminada exitosamente"}
        else:
            mensaje={"mensaje":"No se encontró la empresa"}
        return JsonResponse(mensaje)



class EmpleadoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  
    def get(self,request,usuario=""):
        if len(usuario)>0:
            Emp=list(Empleado.objects.filter(usuario=usuario).values())
            if len(Emp)>0:
                datos={'mensaje':Emp}
            else:
                datos={'mensaje':"No se encontró al empleado."}
        else:
            Emp=list(Empleado.objects.values())
            if len(Emp)>0:
                datos={"mensaje":Emp}
            else:
                datos={"mensaje":"No se encontraron empleados."}
        return JsonResponse(datos)

    def post(self,request):
        data=json.loads(request.body)
        try:
            Empr=Empresas.objects.get(empresa=data["empresa"])
            Emp=Empleado.objects.create(empresa=Empr)
            Emp.save()
            mensaje={"Mensaje":"Prestamo Registrado."}
        except Empresas.DoesNotExist:
            mensaje={"Mensaje":"La empresa no existe."}
        return JsonResponse(mensaje)
        '''Emp=Empleado(usuario=data['usuario'],nombre=data['nombre'], 
        apellido=data['apellido'],email=data['email'],celular=data['celular'],
        fecha_nac=data['fecha_nac'],contraseña=data['contraseña'],codigo=data['codigo'],
        empresa=data['empresa'])
        Emp.save()
        datos={"mensaje":"Empleado registrado exitosamente."}
        return JsonResponse(datos)'''
    
    def put(self,request,usuario):
        data=json.loads(request.body)
        Emp=list(Empleado.objects.filter(usuario=usuario).values())
        if len(Emp)>0:
            Empl=Empleado.objects.get(usuario=usuario)
            Empl.nombre=data["nombre"]
            Empl.apellido=data["apellido"]
            Empl.email=data["email"]
            Empl.celular=data["celular"]
            Empl.fecha_nac=data["fecha_nac"]
            Empl.contraseña=data["contraseña"]
            Empl.codigo=data["codigo"]
            Empl.empresa=data["empresa"]
            Empl.save()
            mensaje={"mensaje":"Empleado actualizado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontró al empleado."}
        return JsonResponse(mensaje)

    def delete(self,request,usuario):
        Emp=list(Empleado.objects.filter(usuario=usuario).values())
        if len(Emp)>0:
            Empleado.objects.filter(usuario=usuario).delete()
            mensaje={"mensaje":"Empleado elminado exitosamente"}
        else:
            mensaje={"mensaje":"No se encontró al empleado"}
        return JsonResponse(mensaje)

