from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cargando_view(request):
    return render(request, 'cargando.html')
