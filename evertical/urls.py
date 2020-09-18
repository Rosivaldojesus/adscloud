from django.urls import path
from .views import index, clientes, base, model_header, model_footer

urlpatterns = [
    path('', index),
    path('clientes/', clientes),
    path('base/', base),
    path('model_header/', model_header)
    path('model_footer/', model_footer)
]