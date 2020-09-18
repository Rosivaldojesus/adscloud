from django.urls import path
from .views import index, clientes

urlpatterns = [
    path('', index),
    path('clientes/', clientes)
]