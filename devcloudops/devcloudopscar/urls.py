from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
]
