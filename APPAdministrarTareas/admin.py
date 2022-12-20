from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Materia)

admin.site.register(Persona)

admin.site.register(CarreraUniversitaria)

admin.site.register(EstudianteCarrera)

admin.site.register(CursoUniversidad)

admin.site.register(Matricula)


