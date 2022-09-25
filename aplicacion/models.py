from django.db import models

# Create your models here.
class Empresas(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nombre=models.TextField(max_length=30,null=False)
    ubicacion=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,unique=True)
    nit=models.IntegerField(null=False)
    ciudad=models.CharField(max_length=45,null=False)
    telefono=models.IntegerField(null=False)
    sector_p=models.CharField(max_length=45,null=False)
    fecha_cre=models.DateField(auto_now=True)

class Empleado(models.Model):
    usuario=models.CharField(max_length=30, primary_key=True)
    nombre=models.TextField(max_length=20,null=False)
    apellido=models.TextField(max_length=20,null=False)
    email=models.EmailField(max_length=45,unique=True)
    celular=models.CharField(max_length=20)
    fecha_nac=models.DateField(null=True)
    contraseña=models.CharField(max_length=18)
    codigo=models.IntegerField(null=False)
    fecha_cre=models.DateField(auto_now=True)
    empresa=models.ForeignKey(Empresas, on_delete=models.CASCADE)
    
class Movimientos(models.Model):
    empresa=models.CharField(max_length=45,primary_key=True)
    codigo_mov=models.IntegerField(auto_created=True)
    ingresos=models.IntegerField(null=False)
    egresos=models.IntegerField(null=False)
    fecha_hora=models.DateField(auto_now=True)
    usuario=models.CharField(max_length=30, null=False)


    
class Administrador(models.Model):
    usuario=models.CharField(max_length=30, primary_key=True)
    email=models.EmailField(max_length=45,unique=True)
    contraseña=models.CharField(max_length=18)
    fecha_cre=models.DateField(auto_now=True)
    
class Login(models.Model):
    contador=models.IntegerField(primary_key=True)
    usuario=models.ForeignKey(Administrador,on_delete=models.CASCADE)
    contraseña=models.CharField(max_length=18)

class Gerente(models.Model):
    usuario=models.CharField(max_length=30, primary_key=True)
    contraseña=models.CharField(max_length=18)
    empresa=models.CharField(max_length=45)
    codigo=models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    email=models.EmailField(max_length=45,unique=True)
    fecha_cre=models.DateField(auto_now=True)


    