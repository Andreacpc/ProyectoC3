from django.db import models

# Create your models here.
class Empresas(models.Model):
    codigo=models.AutoField(primary_key=True)
    empresa=models.TextField(max_length=30,null=False)
    ubicacion=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,unique=True)
    nit=models.IntegerField(null=False)
    ciudad=models.CharField(max_length=45,null=False)
    telefono=models.IntegerField(null=False)
    sector_p=models.CharField(max_length=45,null=False)
    fecha_cre=models.DateField(auto_now=True)

    def __str__(self):
        return self.empresa

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
    
    def __str__(self):
        return self.usuario
    
class Movimientos(models.Model):
    codigo_mov=models.AutoField(primary_key=True)
    ingresos=models.IntegerField(null=False)
    egresos=models.IntegerField(null=False)
    fecha_hora=models.DateField(auto_now=True)
    concepto=models.TextField(max_length=45,null=True)
    usuario=models.ForeignKey(Empleado, on_delete=models.CASCADE)
    empresa=models.ForeignKey(Empresas, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.codigo_mov

  
class Administrador(models.Model):
    usuario=models.CharField(max_length=30, primary_key=True)
    email=models.EmailField(max_length=45,unique=True)
    contraseña=models.CharField(max_length=18)
    fecha_cre=models.DateField(auto_now=True)

    def __str__(self):
        return self.usuario
    
class Login(models.Model):
    contador=models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=30,unique=True)
    contraseña=models.CharField(max_length=18)

    def __str__(self):
        return self.usuario

class Gerente(models.Model):
    usuario=models.CharField(max_length=30, primary_key=True)
    contraseña=models.CharField(max_length=18)
    empresa=models.ForeignKey(Empresas, on_delete=models.CASCADE)
    codigo=models.IntegerField(null=False)
    email=models.EmailField(max_length=45,unique=True)
    fecha_cre=models.DateField(auto_now=True)

    def __str__(self):
        return self.usuario


    