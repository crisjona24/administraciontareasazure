from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# Pagina Principal
def principal(request):
    return render(request, "index.html")

# Cuenta
def cuenta(request):
    return render(request, "cuenta.html")

def registrarCuenta(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    correo = request.POST['txtCorreo']
    celular = request.POST['txtCelular']
    cedula = request.POST['txtCedula']
    user = request.POST['usuario']
    contra = request.POST['clave']

    persona = Persona.objects.create(
        nombre=nombre, apellido=apellido, correo=correo, celular=celular, cedula = cedula, user=user, contra=contra)
    return redirect('/tareas/Administrador/')

def validar(request):
    if request.GET["username"] and request.GET["clave"]:
        usuario = request.GET["username"]
        clave = request.GET["clave"]
        if len(usuario)>0 and len(clave)>0:
            personaU = Persona.objects.filter(user__icontains=usuario)
            personaC = Persona.objects.filter(contra__icontains=clave)
            if(personaC and personaU):
                messages.success(request, F"Bienvenido a la administracion")
                return redirect(to="/tareas/")
            else:
                return redirect(to="/tareas/Administrador/")
        elif len(usuario)==0 or len(clave)==0:
            messages.error(request, F"Error cree una cuenta")
            return redirect(to="/tareas/Administrador/")
    else:
        return redirect(to="/tareas/Administrador/")

# Administracion de Cursos
def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Curso registrado!')
    return redirect('/tareas/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/tareas/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/tareas/')

def listadoCursos(request):
    cursos = Curso.objects.all()
    messages.success(request, 'Cursos listados!')
    return render(request, "listadoCursos.html", {"cursos": cursos})

def verCurso(request, codigo): #ver equipo
    #busca en el modelo correspondiente para poder ver la informacion
    curso = Curso.objects.get(codigo = codigo)
    return render(request,'verCurso.html',{"cursos":curso})

# Administracion de Estudiantes
def estudiante(request):
    return render(request, "gestionEstudiante.html")

def registrarEstudiantes(request):
    nombreE = request.POST['txtNombre']
    apellidoE = request.POST['txtApellido']
    correoE = request.POST['txtCorreo']
    celularE = request.POST['txtCelular']
    cedulaE = request.POST['txtCedula']
    user = request.POST['usuario']
    carrera_E = request.POST['carrera']

    estudiante = Estudiante.objects.create(
        nombreE=nombreE, apellidoE=apellidoE, correoE=correoE, celularE=celularE, cedulaE = cedulaE, user=user, carrera_E=carrera_E)
    return redirect('/tareas/listadoEstudiantes/')

def listadoEstudiantes(request):
    estudianteListados = Estudiante.objects.all()
    messages.success(request, '¡Estudiantes listados!')
    return render(request, "listadoEstudiantes.html", {"cursos": estudianteListados})

def eliminarEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect('/tareas/listadoEstudiantes/')

def edicionEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, "edicionEstudiante.html", {"curso": estudiante})

def editarEstudiante(request):
    #id = request.POST['id']
    nombreE = request.POST['txtNombre']
    apellidoE = request.POST['txtApellido']
    correoE = request.POST['txtCorreo']
    celularE = request.POST['txtCelular']
    cedulaE = request.POST['txtCedula']
    user = request.POST['usuario']
    carrera_E = request.POST['carrera']

    estudiante = Estudiante.objects.get(id=id)
    estudiante.nombreE = nombreE
    estudiante.apellidoE = apellidoE
    estudiante.correoE = correoE
    estudiante.celularE = celularE
    estudiante.cedulaE = cedulaE
    estudiante.user = user
    estudiante.carrera_E = carrera_E

    estudiante.save()
    messages.success(request, '¡Estudiante actualizado!')
    return redirect('/tareas/listadoEstudiantes')

def verEstudiante(request, id): #ver equipo
    #busca en el modelo correspondiente para poder ver la informacion
    estudiante = Estudiante.objects.filter(id__icontains=id)
    return render(request,'verEstudiante.html',{"cursos":estudiante})


# Administracion de Profesores
def profesor(request):
    return render(request, "gestionProfesor.html")

def registrarProfesores(request):
    nombreP = request.POST['txtNombre']
    apellidoP = request.POST['txtApellido']
    correoP = request.POST['txtCorreo']
    celularP = request.POST['txtCelular']
    cedulaP = request.POST['txtCedula']
    user = request.POST['usuario']
    carrera_P = request.POST['carrera']

    profesor = Profesor.objects.create(
        nombreP=nombreP, apellidoP=apellidoP, correoP=correoP, celularP=celularP, cedulaP = cedulaP, user=user, carrera_P=carrera_P)
    return redirect('/tareas/listadoProfesores/')

def listadoProfesores(request):
    profesoresListados = Profesor.objects.all()
    messages.success(request, 'Profesores listados!')
    return render(request, "listadoProfesores.html", {"cursos": profesoresListados})

def eliminarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return redirect('/tareas/listadoProfesores/')

def edicionProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    return render(request, "edicionProfesor.html", {"curso": profesor})

def editarProfesor(request):
    id = request.POST['id']
    nombreP = request.POST['txtNombre']
    apellidoP = request.POST['txtApellido']
    correoP = request.POST['txtCorreo']
    celularP = request.POST['txtCelular']
    cedulaP = request.POST['txtCedula']
    user = request.POST['usuario']
    carrera_P = request.POST['carrera']

    profesor = Profesor.objects.get(id=id)
    profesor.nombreP = nombreP
    profesor.apellidoP = apellidoP
    profesor.correoP = correoP
    profesor.celularP = celularP
    profesor.cedulaP = cedulaP
    profesor.user = user
    profesor.carrera_P = carrera_P

    profesor.save()
    messages.success(request, '¡Profesor actualizado!')
    return redirect('/tareas/listadoProfesores/')

def verProfesor(request, id): #ver profesor
    #busca en el modelo correspondiente para poder ver la informacion
    profesor = Profesor.objects.filter(id__icontains=id)
    return render(request,'verProfesor.html',{"cursos":profesor})


# Administracion de Materias
def materia(request):
    return render(request, "gestionMateria.html")

def registrarMaterias(request):
    nombreM = request.POST['txtNombre']
    nroHoras = request.POST['txtHoras']
    nombreProfesor = request.POST['txtProfesor']
    nroCreditos = request.POST['txtCreditos']
    cadena_M = request.POST['txtcadena']
    ciclo_M = request.POST['ciclo']

    materia = Materia.objects.create(
        nombreM=nombreM, nroHoras=nroHoras, nombreProfesor=nombreProfesor, nroCreditos=nroCreditos, cadena_M = cadena_M, ciclo_M=ciclo_M)
    return redirect('/tareas/listadoMaterias/')

def listadoMaterias(request):
    materiaListado = Materia.objects.all()
    messages.success(request, 'Materias listadas!')
    return render(request, "listadoMaterias.html", {"cursos": materiaListado})

def eliminarMateria(request, id):
    materia = Materia.objects.get(id=id)
    materia.delete()
    return redirect('/tareas/listadoMaterias/')

def edicionMateria(request, id):
    materia = Materia.objects.get(id=id)
    return render(request, "edicionMateria.html", {"curso": materia})

def editarMateria(request):
    id = request.POST['id']
    nombreM = request.POST['txtNombre']
    nroHoras = request.POST['txtHoras']
    nombreProfesor = request.POST['txtProfesor']
    nroCreditos = request.POST['txtCreditos']
    cadena_M = request.POST['txtcadena']
    ciclo_M = request.POST['ciclo']

    materia = Materia.objects.get(id=id)
    materia.nombreM = nombreM
    materia.nroHoras = nroHoras
    materia.nombreProfesor = nombreProfesor
    materia.nroCreditos = nroCreditos
    materia.cadena_M = cadena_M
    materia.ciclo_M = ciclo_M

    materia.save()
    messages.success(request, '¡Materia actualizado!')
    return redirect('/tareas/listadoMaterias/')

def verMateria(request, id): #ver materia
    #busca en el modelo correspondiente para poder ver la informacion
    materia = Materia.objects.filter(id__icontains=id)
    return render(request,'verMateria.html',{"cursos":materia})


# Administracion de Contacto

def contacto(request):
    #Renderizamos la pagina de contacto
    return render(request, "Contacto.html")


## Login de Administrador

def login(request):
    #Renderizamos la pagina de login
    return render(request, "loginAdmin.html")

#
#
# CURSOS PRIVADOS 
#
#

# Administracion de Carreras
def carreraUniversidad(request):
    carreraListada = CarreraUniversitaria.objects.all()
    messages.success(request, '¡Carreras listadas!')
    return render(request, "gestionCarrera.html", {"cursos": carreraListada})

def registrarCarreraUniversidad(request):
    codigoCarrera = request.POST['txtCodigo']
    nombreCarrera = request.POST['txtNombre']
    duracionCarrera = request.POST['txtDuracion']
    descripcionCarrera = request.POST['txtDescrip']

    carreraU = CarreraUniversitaria.objects.create(
        codigoCarrera=codigoCarrera, nombreCarrera=nombreCarrera, duracionCarrera=duracionCarrera, descripcionCarrera=descripcionCarrera)
    messages.success(request, '¡Carrera registrada!')
    return redirect('/tareas/carrera/')

def edicionCarrera(request, codigoCarrera):
    carrera = CarreraUniversitaria.objects.get(codigoCarrera=codigoCarrera)
    return render(request, "edicionCarrera.html", {"curso": carrera})

def editarCarrera(request):
    codigoCarrera = request.POST['txtCodigo']
    nombreCarrera = request.POST['txtNombre']
    duracionCarrera = request.POST['txtDuracion']
    descripcionCarrera = request.POST['txtDescrip']

    carrera = CarreraUniversitaria.objects.get(codigoCarrera=codigoCarrera)
    carrera.nombreCarrera = nombreCarrera
    carrera.duracionCarrera = duracionCarrera
    carrera.descripcionCarrera = descripcionCarrera
    carrera.save()
    messages.success(request, '¡Carrera actualizado!')
    return redirect('/tareas/carrera/')

def eliminarCarrera(request, codigoCarrera):
    carrera = CarreraUniversitaria.objects.get(codigoCarrera=codigoCarrera)
    carrera.delete()
    messages.success(request, '¡Carrera eliminado!')
    return redirect('/tareas/carrera/')

# Administracion de Estudiante U
def estudianteUniversidad(request):
    estudianteListada = EstudianteCarrera.objects.all()
    messages.success(request, '¡Estudiantes listados!')
    return render(request, "gestionEstudianteC.html", {"cursos": estudianteListada})

def estudiantesU(request):
    estudianteListada = EstudianteCarrera.objects.all()
    messages.success(request, '¡Estudiantes listados!')
    return render(request, "listadoEstudiantesC.html", {"cursos": estudianteListada})

def registrarEstudianteUniversidad(request):
    cedula = request.POST['txtCodigo']
    apellidoPaterno = request.POST['txtApellido1']
    apellidoMaterno = request.POST['txtApellido2']
    nombresEstudiante = request.POST['txtNombre']
    fechaNacimiento = request.POST['txtFecha']
    sexo = request.POST['sexo']
    carreraUniversitaria = request.POST['txtCarrera']
    valido = 1

    carreraListada = CarreraUniversitaria.objects.all()
    for c in carreraListada:
        if c.nombreCarrera == carreraUniversitaria:
            valido = 0
            print('Es igual')
            id = c.nombreCarrera
            estudiante = EstudianteCarrera.objects.create( cedula=cedula, apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno, nombresEstudiante=nombresEstudiante
            , fechaNacimiento=fechaNacimiento, sexo = sexo, vigenciaEstudiante= 1, carreraUniversitaria = id)
            messages.success(request, '¡Estudiante registrado!')
            return redirect('/tareas/estudianteC/')
    if valido == 1:
        messages.success(request, '¡Error al registrar estudiante!')
        return redirect('/tareas/estudianteC/')

def edicionEstudianteC(request, cedula):
    estudi = EstudianteCarrera.objects.get(cedula=cedula)
    return render(request, "edicionEstudianteC.html", {"curso": estudi})

def editarEstudianteC(request):
    cedula = request.POST['txtCodigo']
    apellidoPaterno = request.POST['txtApellido1']
    apellidoMaterno = request.POST['txtApellido2']
    nombresEstudiante = request.POST['txtNombre']
    fechaNacimiento = request.POST['txtFecha']
    sexo = request.POST['sexo']
    carreraUniversitaria = request.POST['txtCarrera']

    estudi = EstudianteCarrera.objects.get(cedula=cedula)
    estudi.apellidoPaterno = apellidoPaterno
    estudi.apellidoMaterno = apellidoMaterno
    estudi.nombresEstudiante = nombresEstudiante
    estudi.fechaNacimiento = fechaNacimiento
    estudi.sexo = sexo
    estudi.carreraUniversitaria = carreraUniversitaria
    estudi.save()
    messages.success(request, '¡Estudiante actualizado!')
    return redirect('/tareas/estudianteC/')

def eliminarEstudianteC(request, cedula):
    estudi = EstudianteCarrera.objects.get(cedula=cedula)
    estudi.delete()
    messages.success(request, '¡Estudiante eliminado!')
    return redirect('/tareas/estudianteC/')
  
# Administracion de Curso
def cursoUniversidad(request):
    cursoListada = CursoUniversidad.objects.all()
    messages.success(request, '¡Cursos listadas!')
    return render(request, "gestionCurso.html", {"cursos": cursoListada})

def cursos(request):
    cursoListada = CursoUniversidad.objects.all()
    messages.success(request, '¡Cursos listadas!')
    return render(request, "listadoCursosC.html", {"cursos": cursoListada})

def registrarCursoUniversidad(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    docente = request.POST['docente']

    curso = CursoUniversidad.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos, docente = docente)
    messages.success(request, '¡Curso registrado!')
    return redirect('/tareas/cursoU/')

def edicionCursoU(request, codigo):
    curso = CursoUniversidad.objects.get(codigo=codigo)
    return render(request, "edicionCursoC.html", {"curso": curso})

def editarCursoU(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    docente = request.POST['docente']

    curso = CursoUniversidad.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.docente = docente
    curso.save()
    messages.success(request, '¡Curso actualizado!')
    return redirect('/tareas/cursoU/')

def eliminarCursoU(request, codigo):
    curso = CursoUniversidad.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso eliminado!')
    return redirect('/tareas/cursoU/')

# Administracion de Matricula
def matricula(request):
    matricula = Matricula.objects.all()
    messages.success(request, '¡Matriculas listadas!')
    return render(request, "gestionMatricula.html", {"cursos": matricula})

def registrarMatricula(request):
    nombre = request.POST['txtEstudi']
    apellido = request.POST['txtEstudi1']
    cursoUniversidad = request.POST['numCarrera']
    fechaMatricula = request.POST['fecha']

    valido = 0

    estudiantes = EstudianteCarrera.objects.all()
    cursos = CursoUniversidad.objects.all()

    for estu in estudiantes:
        if nombre == estu.nombresEstudiante and apellido == estu.apellidoPaterno:
            idEstudiante = estu.cedula
            valido = valido + 1
    for cur in cursos:
        if cursoUniversidad == cur.nombre:
            codigoCurso = cur.codigo
            valido = valido + 1

    if valido == 2:
        matricula = Matricula.objects.create(estudianteCarrera=idEstudiante, cursoUniversidad=codigoCurso, fechaMatricula = fechaMatricula)
        messages.success(request, '¡Matricula registrada!')
        return redirect('/tareas/matricula/')
    else:
        messages.success(request, '¡Error de matricula!')
        return redirect('/tareas/matricula/')

def eliminarMatricula(request, idMatricula):
    matricula = Matricula.objects.get(idMatricula=idMatricula)
    matricula.delete()
    messages.success(request, '¡Matricula eliminada!')
    return redirect('/tareas/matricula/')