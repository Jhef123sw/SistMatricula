from django.contrib import admin
from principal.models import Alumno, Profesor, Curso, Matricula, Dictar, Nota


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo')  # Campos que se muestran en la lista
    search_fields = ('nombre', 'correo')  # Habilita búsqueda por estos campos
    list_filter = ('direccion',)  # Filtros por campo


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo')
    search_fields = ('nombre', 'correo')
    list_filter = ('direccion',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'num_creditos')
    search_fields = ('nombre',)


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo', 'alumno', 'curso')
    search_fields = ('alumno__nombre', 'curso__nombre')  # Soporte para búsquedas por relaciones
    list_filter = ('tipo', 'fecha')


@admin.register(Dictar)
class DictarAdmin(admin.ModelAdmin):
    list_display = ('fecha_ini', 'fecha_ter', 'profesor', 'curso')
    search_fields = ('profesor__nombre', 'curso__nombre')
    list_filter = ('fecha_ini', 'fecha_ter')


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('valor', 'fecha', 'trimestre', 'matricula')
    search_fields = ('matricula__alumno__nombre',)
    list_filter = ('trimestre', 'fecha')
