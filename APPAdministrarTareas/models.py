from email.policy import default
from pickle import FALSE
from random import choices
from secrets import choice
from tokenize import blank_re
from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)

class Estudiante(models.Model):
    carrera = (('sistemas','sistemas'),('computacion','computacion'),('electricidad','electricidad'),('electronica','electronica'),)
    nombreE = models.CharField(max_length=30, blank=False)
    apellidoE = models.CharField(max_length=30, blank=False)
    correoE = models.EmailField()
    celularE = models.CharField(max_length=10, blank=False)
    cedulaE = models.CharField(max_length=10, blank=False)
    user = models.CharField(max_length=15, blank=False)
    carrera_E= models.CharField(max_length=30, choices=carrera, default="", blank=False)

    def __str__(self):
        textoE = "{0} ({1})"
        return textoE.format(self.nombreE, self.apellidoE)

class Profesor(models.Model):
    carrera = (('sistemas','sistemas'),('computacion','computacion'),('electricidad','electricidad'),('electronica','electronica'),)
    nombreP = models.CharField(max_length=30, blank=False)
    apellidoP = models.CharField(max_length=30, blank=False)
    correoP = models.EmailField()
    celularP = models.CharField(max_length=10, blank=False)
    cedulaP = models.CharField(max_length=10, blank=False)
    user = models.CharField(max_length=15, blank=False)
    carrera_P= models.CharField(max_length=30, choices=carrera, default="", blank=False)


    def __str__(self):
        textoP = "{0} ({1})"
        return textoP.format(self.nombreP, self.apellidoP)

class Materia(models.Model):
    ciclo = (('1ero','1ro'),('2do','2do'),('3ro','3ro'),('4to','4to'),('5to','5to'),('6to','6to'),('7mo','7mo'),('8vo','8vo'),)
    nombreM = models.CharField(max_length=30, blank=False)
    nroHoras = models.PositiveSmallIntegerField()
    nombreProfesor = models.CharField(max_length=30, blank=False)
    nroCreditos = models.PositiveSmallIntegerField()
    cadena = (('no','no'),('si','si'),)
    cadena_M = models.CharField(max_length=30, choices=cadena, default="", blank=False)
    ciclo_M= models.CharField(max_length=30, choices=ciclo, default="", blank=False)

    def __str__(self):
        textoM = "{0} ({1})"
        return textoM.format(self.nombreM, self.nroCreditos)

class Persona(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    correo = models.EmailField()
    celular = models.CharField(max_length=10, blank=False)
    cedula = models.CharField(max_length=10, blank=False)
    user = models.CharField(max_length=15, blank=False)
    contra = models.CharField(max_length=15, blank=False)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.apellido)


#Nuevos modelos

class CarreraUniversitaria(models.Model):
    codigoCarrera = models.CharField(primary_key=True, max_length=6,  blank=False)
    nombreCarrera = models.CharField(max_length=30, blank=False)
    duracionCarrera = models.PositiveSmallIntegerField(default=8)
    descripcionCarrera= models.CharField(max_length=80, blank=False)

    def __str__(self):
        textoCarrera = "{0} (Duracion carrera: {1} año(s))"
        return textoCarrera.format(self.nombreCarrera, self.duracionCarrera)

class EstudianteCarrera(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, blank=False)
    apellidoPaterno = models.CharField(max_length=30, blank=False)
    apellidoMaterno = models.CharField(max_length=30, blank=False)
    nombresEstudiante = models.CharField(max_length=30, blank=False)
    fechaNacimiento = models.DateField()
    sexos = [('F','F'),('M','M')]
    sexo = models.CharField(max_length=1, blank=False, choices= sexos, default='F')
    vigenciaEstudiante = models.BooleanField(default=True)
    #carreraUniversitaria = models.ForeignKey(CarreraUniversitaria, null=False, blank=False, on_delete = models.CASCADE)  
    carreraUniversitaria = models.CharField(max_length=30, blank=False)
    def nombreCompleto(self):
        textoNC = "{0} {1}, {2}"
        return textoNC.format(self.apellidoPaterno, self.apellidoMaterno, self.nombresEstudiante)
    
    def __str__(self):
        textoEstudianteC = "{0} / Carrera: {1} / {2}))"
        if self.vigenciaEstudiante:
            estado = "Activo"
        else:
            estado = "De baja"
        return textoEstudianteC.format(self.nombreCompleto(), self.carreraUniversitaria, estado)


class CursoUniversidad(models.Model):
    codigo = models.CharField(primary_key=True, blank = False, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1} / Docente: {2})"
        return texto.format(self.nombre, self.creditos, self.docente)

class Matricula(models.Model):
    idMatricula = models.AutoField(primary_key=True)
    estudianteCarrera = models.ForeignKey(EstudianteCarrera, null=False, blank=False, on_delete = models.CASCADE)  
    cursoUniversidad = models.ForeignKey(CursoUniversidad, null=False, blank=False, on_delete = models.CASCADE)  
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        matricula = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudianteCarrera.sexo == "F":
            sexoL = "a"
        else:
            sexoL = "o"
        return matricula.format(self.estudianteCarrera.nombreCompleto(), sexoL, self.cursoUniversidad, self.fechaMatricula)

