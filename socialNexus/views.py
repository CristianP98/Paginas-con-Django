from django.shortcuts import render

def index(request):
  return render(request, "index.html")

def donaciones(request):
  return render(request, "donaciones.html")

def empresa(request):
  return render(request, "empresa.html")

def login_view(request):
  return render(request, "login.html")

def nosotros(request):
  return render(request, "nosotros.html")

def noticias(request):
  return render(request, "noticias.html")

def ong(request):
  return render(request, "ong.html")

def registro(request):
  return render(request, "registro.html")