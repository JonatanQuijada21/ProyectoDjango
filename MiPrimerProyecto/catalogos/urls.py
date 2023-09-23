from django.urls import path
from .views import *

urlpatterns = [

    path('paises/', PaisListView.as_view(), name='pais_list'),  # Agregada para listar paises
    path('paises/nuevo/', PaisCreateView.as_view(), name='pais_create'), # Agregada para crear paises
    path('paises/<int:pk>/', PaisUpdateView.as_view(), name='pais_update'),# Agregada para actualizar paises
    path('paises/<int:pk>/eliminar/', PaisDeleteView.as_view(), name='pais_delete'), # Agregada para eliminar paises

    path('departamentos/', DepartamentoListView.as_view(), name='departamento_list'), # Agregada para listar departamentos
    path('departamentos/nuevo/', DepartamentoCreateView.as_view(), name='departamento_create'), # Agregada para crear departamentos
    path('departamentos/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'), # Agregada para actualizar departamentos
    path('departamentos/<int:pk>/eliminar/', DepartamentoDeleteView.as_view(), name='departamento_delete'), # Agregada para eliminar departamentos

    path('municipios/', MunicipioListView.as_view(), name='municipio_list'),  # Agregada para listar municipios
    path('municipios/nuevo/', MunicipioCreateView.as_view(), name='municipio_create'),  # Agregada para crear municipios
    path('municipios/<int:pk>/', MunicipioUpdateView.as_view(), name='municipio_update'), #Agregada para actualizar municipios
    path('municipios/<int:pk>/eliminar/', MunicipioDeleteView.as_view(), name='municipio_delete'), # Agregada para eliminar municipios
]
