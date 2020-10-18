from django.urls import path
from . import views


app_name = 'Comida'

urlpatterns = [
    path('salvar/comida', views.registrar_comida),
    path('salvar/ingrediente', views.registrar_ingrediente),
]