from django.urls import path
from django.contrib.auth import views
from django.shortcuts import render

urlpatterns = [
    # path('', view, name""),
    path('login/', views.LoginView.as_view(template_name='usuarios/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),



]