from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.models import Alumno, Profesor, Curso, Matricula, Dictar, Nota
from principal.forms import AlumnoForm, CursoForm, ProfesorForm, ContactoForm, MatriculaForm

# Vistas
@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})

@login_required
def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})

@login_required
def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'lista_profesores.html', {'profesores': profesores})

@login_required
def dato_alumno(request, id_alumno):
    dato = get_object_or_404(Alumno, pk=id_alumno)
    dato2 = Matricula.objects.filter(alumno=id_alumno)
    return render(request, 'dato_alumno.html', {'alumno': dato, 'cursos_matriculados': dato2})

@login_required
def dato_curso(request, id_curso):
    dato = get_object_or_404(Curso, pk=id_curso)
    dato2 = Matricula.objects.filter(curso=id_curso)
    return render(request, 'dato_curso.html', {'curso': dato, 'alumnos_matriculados': dato2})

@login_required
def dato_profesor(request, id_profesor):
    dato = get_object_or_404(Profesor, pk=id_profesor)
    dato2 = Dictar.objects.filter(profesor=id_profesor)
    return render(request, 'dato_profesor.html', {'profesor': dato, 'cursos_dictados': dato2})

@login_required
def nuevo_alumno(request):
    if request.method == 'POST':
        formulario = AlumnoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_alumnos')
    else:
        formulario = AlumnoForm()
    return render(request, 'alumnoform.html', {'formulario': formulario})

@login_required
def nuevo_curso(request):
    if request.method == 'POST':
        formulario = CursoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_cursos')
    else:
        formulario = CursoForm()
    return render(request, 'cursoform.html', {'formulario': formulario})

@login_required
def nuevo_profesor(request):
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_profesores')
    else:
        formulario = ProfesorForm()
    return render(request, 'profesorform.html', {'formulario': formulario})

@login_required
def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el sistema'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a:' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@gmail.com'])
            correo.send()
            return redirect('inicio')
    else:
        formulario = ContactoForm()
    return render(request, 'contactoform.html', {'formulario': formulario})

@login_required
def nueva_matricula(request):
    alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()
    if request.method == 'POST':
        formulario = MatriculaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_matriculas')
    else:
        formulario = MatriculaForm()
    return render(request, 'matriculaform.html', {'formulario': formulario, 'alumnos': alumnos, 'cursos': cursos})

@login_required
def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('nuevo_usuario')
    else:
        formulario = UserCreationForm()
    return render(request, 'nuevousuario.html', {'formulario': formulario})

@login_required
def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/privado/")
            else:
                return render('noactivo.html', request)
        else:
            return render('nousuario.html',request)

@login_required
def perfil(request, username):
    usuario = request.user
    usuario_no_logueado = User.objects.get(username=username)
    if usuario == User.objects.get(username=username):
        return render('perfil.html', {'usuario':usuario}, request)
    else:
        return render('perfil_no_logueado.html', {'usuario':usuario_no_logueado}, request) 


@login_required
def ingresar(request):
    if request.user.is_authenticated:
        return redirect('privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('privado')
    else:
        formulario = AuthenticationForm()
    return render(request, 'ingresar.html', {'formulario': formulario})


@login_required(login_url='ingresar')
def privado(request):
    return render(request, 'privado.html', {'usuario': request.user})


@login_required(login_url='ingresar')
def cerrar(request):
    logout(request)
    return redirect('ingresar')


@login_required
def editar_alumno(request, object_id):
    alumno = get_object_or_404(Alumno, id=object_id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form, 'alumno': alumno})
