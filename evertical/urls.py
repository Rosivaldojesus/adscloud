from django.urls import path
from .views import index, clientes, base

urlpatterns = [
    path('', index),
    path('clientes/', clientes),
    path('base/', base),
]