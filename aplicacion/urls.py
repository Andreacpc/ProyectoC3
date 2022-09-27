from django.urls import path
from aplicacion.views import EmpleadoView
from aplicacion.views import EmpresaView

urlpatterns= [
    path('Empleado/',EmpleadoView.as_view(),name='Listar'),
    path('Empleado/<str:usuario>',EmpleadoView.as_view(),name='Buscar'),
    path('Empresa/',EmpresaView.as_view(),name='Listar'),
    path('Empresa/<str:codigo>',EmpresaView.as_view(),name='Buscar')
]
