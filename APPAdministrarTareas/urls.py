from django.urls import path
from . import views

urlpatterns = [

    ##
    ##
    ##PRINCIPAL
    ##
    ##

    # Cursos
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('listadoCursos/', views.listadoCursos),
    path('verCurso/<codigo>', views.verCurso),
    
    # Estudiante
    path('listadoEstudiantes/', views.listadoEstudiantes),
    path('estudiante/', views.estudiante),
    path('registrarEstudiantes/', views.registrarEstudiantes),
    path('eliminarEstudiante/<id>', views.eliminarEstudiante),
    path('edicionEstudiante/<id>', views.edicionEstudiante),
    path('editarEstudiante/', views.editarEstudiante),
    path('verEstudiante/<id>', views.verEstudiante),

    # Profesor
    path('listadoProfesores/', views.listadoProfesores),
    path('profesor/', views.profesor),
    path('registrarProfesores/', views.registrarProfesores),
    path('eliminarProfesor/<id>', views.eliminarProfesor),
    path('edicionProfesor/<id>', views.edicionProfesor),
    path('editarProfesor/', views.editarProfesor),
    path('verProfesor/<id>', views.verProfesor),

    # Materia
    path('listadoMaterias/', views.listadoMaterias),
    path('materia/', views.materia),
    path('registrarMaterias/', views.registrarMaterias),
    path('eliminarMateria/<id>', views.eliminarMateria),
    path('edicionMateria/<id>', views.edicionMateria),
    path('editarMateria/', views.editarMateria),
    path('verMateria/<id>', views.verMateria),

    # Cuenta
    path('cuenta/', views.cuenta),
    path('registrarCuenta/', views.registrarCuenta),
    path('validacion/', views.validar),

    # Contacto
    path('contacto/', views.contacto),

    # Login
    path('Administrador/', views.login),

    #
    #
    # ALTERNAS
    #
    #
    #
        
    # Carrera
    path('carrera/', views.carreraUniversidad),
    path('registrarCarrera/', views.registrarCarreraUniversidad),
    path('edicionCarrera/<codigoCarrera>', views.edicionCarrera),
    path('editarCarrera/', views.editarCarrera),
    path('eliminarCarrera/<codigoCarrera>', views.eliminarCarrera),

    # Estudiante C
    path('estudianteC/', views.estudianteUniversidad),
    path('registrarEstudianteC/', views.registrarEstudianteUniversidad),
    path('edicionEstudianteC/<cedula>', views.edicionEstudianteC),
    path('editarEstudianteC/', views.editarEstudianteC),
    path('eliminarEstudianteC/<cedula>', views.eliminarEstudianteC),
    path('listadoEstudiantesC/', views.estudiantesU),

    # Curso C
    path('cursoU/', views.cursoUniversidad),
    path('registrarCursoUniversidad/', views.registrarCursoUniversidad),
    path('edicionCursoC/<codigo>', views.edicionCursoU),
    path('editarCursoC/', views.editarCursoU),
    path('eliminarCursoC/<codigo>', views.eliminarCursoU),
    path('listadoCursosC/', views.cursos),

    # Matricula C
    path('matricula/', views.matricula),
    path('registrarMatricula/', views.registrarMatricula),
    path('eliminarEstudianteC/<idMatricula>', views.eliminarMatricula),

]