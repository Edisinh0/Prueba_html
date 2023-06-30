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
    return render(request,'registration/login.html')

def registro(request):
    return render(request,'registration/registro.html')

def crud(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(request, 'alumnos_list.html', context)

def alumnosAdd(request):
    if request.method != "POST":
        # no es un POST por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'alumnos_add.html', context)
    
    else:
        print("--->>>> llego al else de addAlumnos crea el objeto ")
        # Es un POST, por lo tanto se recuperan los datos del formulario
        # y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"  # ---> esta linea no será tomada en cuenta en la creación dado que se asigna 1 arbitrariamente

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Alumno.objects.create(rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1)
        obj.save()
        context = {"mensaje": "OK, datos grabados..."}
        return render(request, 'alumnos_add.html', context)
    
def alumnos_del(request, pk):
    context = {}
    try:
        alumno = Alumno.objects.get(rut=pk)
        print("REGISTRO A ELIMINAR============>>>")
        print(alumno)
        alumno.delete()
        print("ELIMINADOR============>>>")
        mensaje = "Bien, dato eliminado!!!"
        alumnos = Alumno.objects.all()
        context = {"alumnos": alumnos, "mensaje": mensaje}
        return render(request, "alumnos_list.html", context)
    except:
        mensaje = "Error, el rut  no existe!!!"
        alumnos = Alumno.objects.all()
        context = {"alumnos": alumnos, "mensaje": mensaje}
        return render(request, "alumnos_list.html", context)
    
def alumnos_findEdit(request, pk):
    if pk != "":
        alumno = Alumno.objects.get(rut=pk)
        print(alumno)
        generos = Genero.objects.all()
        print("generos--->>>")
        print(generos)

        print(type(alumno.id_genero.genero))
        context = {"alumno": alumno, "generos": generos}
        if alumno:
            return render(request, "alumnos_edit.html", context)
        else:
            context = {"mensaje": "Error, rut no existe"}
            return render(request, "alumnos_list.html", context)