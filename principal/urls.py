from django.urls import path
from principal import views

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('dato-alumno/<int:id_alumno>/', views.dato_alumno, name='dato_alumno'),
    path('dato-curso/<int:id_curso>/', views.dato_curso, name='dato_curso'),
    path('dato-profesor/<int:id_profesor>/', views.dato_profesor, name='dato_profesor'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('dato-alumno/nuevo/', views.nuevo_alumno, name='nuevo_alumno'),
    path('nuevocur/', views.nuevo_curso, name='nuevo_curso'),
    path('nuevoprof/', views.nuevo_profesor, name='nuevo_profesor'),
    path('contactenos/', views.contacto, name='contacto'),
    path('matriculas/', views.nueva_matricula, name='nueva_matricula'),
    path('usuario/nuevo/', views.nuevo_usuario, name='nuevo_usuario'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('privado/', views.privado, name='privado'),
    path('cerrar/', views.cerrar, name='cerrar'),
    #path('', views.p, name='login'),
    path('<str:username>/', views.perfil, name='perfil'),
    path('alumnos/editar/<int:object_id>/', views.editar_alumno, name='editar_alumno'),
]
