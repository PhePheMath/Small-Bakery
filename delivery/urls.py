from django.urls import path
from . import views


app_name = 'Delivery'

urlpatterns = [
    path('salvar/pedido', views.novo_pedido),
]