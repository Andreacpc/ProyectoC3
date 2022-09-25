from django.contrib import admin

# Register your models here.
from aplicacion.models import Empresas
from aplicacion.models import Movimientos
from aplicacion.models import Empleado
from aplicacion.models import Gerente
from aplicacion.models import Administrador
from aplicacion.models import Login

admin.site.register(Empresas)
admin.site.register(Movimientos)
admin.site.register(Empleado)
admin.site.register(Gerente)
admin.site.register(Administrador)
admin.site.register(Login)

