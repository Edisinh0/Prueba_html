from django.shortcuts import render
from .models import Alumno,Genero
# Create your views here.

def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,'index.html', context)


def contacto(request):
    return render(request,'contacto.html')

def catalogo(request):
    return render(request,'catalogo.html')

def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registro.html')