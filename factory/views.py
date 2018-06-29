from django.shortcuts import render

def login(request):
    return render(request, 'servicefactoryusers/login.html', {})

def index(request):
    return render(request, 'servicefactoryusers/index.html', {})

def tarea(request):
    return render(request, 'servicefactoryusers/tarea.html', {})

def horas(request):
    return render(request, 'servicefactoryusers/horas.html', {})
