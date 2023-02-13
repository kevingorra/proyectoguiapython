from django.shortcuts import render

from web.formularios.formularioMedico import FormularioMedico

from web.models import Medicos

# Create your views here.
# renderizar es PINTAR
def Home(request):
    return render(request,'index.html')

def MedicosVista(request):

    #creamos una variable para controlar la
    #ejec de la alerta
    lanzandoAlerta=False

    #Debo utilizar la clase formularioMedico
    #CREAMOS ASI UN OBJETO
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario,
        "bandera":lanzandoAlerta
    }

    #ACTIVAR LA RECEPCION DE DATOS
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturamos los datos
            datos=datosRecibidos.cleaned_data
            #LLevar mis datos hacia la BD
            medicoNuevo=Medicos(
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"]
            )
            medicoNuevo.save()
            diccionario["bandera"]=True
           


    return render(request,'registromedicos.html',diccionario)

