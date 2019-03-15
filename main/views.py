from django.shortcuts import render, redirect
from .models import Archivo, Estatico, Noticia, Trabajo, Empleado, Curriculum, Solicitud
from .forms import Contacto, Ingreso, Peticion, ActualizarCurriculum
import datetime
from django.core.mail import send_mail

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

def index(request):
	context = {}
	
	context['logo'] = Estatico.objects.latest('telefono1')

	#print(context['list'])
	return render(request, 'main/index.html',context)
	
 
def acerca(request):
	context = {}
	context['logo'] = Estatico.objects.latest('telefono1')
	return render(request, 'main/acerca.html',context)

		
def servicios(request):
	#return render(request, 'main/contact__.html',context)
	#return render(request, 'main/empresa__.html',context)
	context = {}
	context['logo'] = Estatico.objects.latest('telefono1')
	return render(request, 'main/servicios.html',context)


def beneficios(request):
	context = {}
	context['logo'] = Estatico.objects.latest('telefono1')
	
	return render(request, 'main/Beneficios__.html' , context)



def contacto(request):
	context = {}
	context['mensaje'] = ''
	context['info'] = Estatico.objects.all()[:1]
	context['logo'] = Estatico.objects.latest('telefono1')
	
	if request.method == "POST":
		form = Contacto(request.POST, request.FILES)
		if form.is_valid():
			#guardar contacto
			documento = form.cleaned_data['archivo']
			user = form.cleaned_data['nombre']
			#print(user)
			correo = form.cleaned_data['correo']
			numero = form.cleaned_data['numero']
			texto = form.cleaned_data['texto']
			filtro_nombre = Curriculum.objects.filter(nombre=user)
			filtro_correo = Curriculum.objects.filter(correo=correo)
			if len(filtro_correo) > 0:
				context['mensaje'] = 'Ya esta asociado el correo con otra hoja de vida.'				
			elif len(filtro_nombre) > 0:
				context['mensaje'] = 'Ya esta asociado el nombre con otra hoja de vida.'
			else:				
				 
				registro = Curriculum(nombre=user, correo=correo, telefono1=numero, texto=texto, documento=documento)
				registro.save()

				context['mensaje'] = 'Hemos guardado su hoja de vida y su informacion de contacto, por favor espere a que nos comuniquemos con usted.'

	form = Contacto()
	context['form'] = form
	#return render(request, 'main/contact.html',context)
	return render(request, 'main/contacto.html',context)


@login_required
def perfil(request):
	context= {}	
	context['logo'] = Estatico.objects.latest('telefono1')
	context['mensaje'] = ''
	cedula = request.user.empleado.cedula
	#print(request.POST)
	
	if request.method == "POST":
		if 'file' in request.POST:
			form = ActualizarCurriculum(request.POST, request.FILES)
			print(form.errors)
			if form.is_valid():

				documento = form.cleaned_data['documento']
				t = Empleado.objects.get(cedula=cedula)
				t.curriculum = documento
				t.save()
				
				context['confirmacion']= "Tu hoja de vida se ha actualizado"
		else:
			form = Peticion(request.POST)
			if form.is_valid():
				tipo = form.cleaned_data['seleccion']
				user = Empleado.objects.get(cedula=cedula)
				sin_revisar = len(Solicitud.objects.filter(empleado__cedula=cedula, tipo=tipo, estado='Sin revisar'))
				en_proceso 	= len(Solicitud.objects.filter(empleado__cedula=cedula, tipo=tipo, estado='Sin revisar'))
				if sin_revisar > 0 or en_proceso > 0:
					context['mensaje'] = 'Ya existe una solicitud en proceso de este tipo'			
					
				else:
					context['mensaje'] = ''
					
					registro = Solicitud(empleado=user ,tipo= tipo ,fecha=datetime.datetime.now()) 
					registro.save()
				#print(tipo)
	

	context['form'] = Peticion()
	context['file'] = ActualizarCurriculum()
	context['empleado'] = Empleado.objects.filter(cedula=cedula)
	context['documentos'] = Archivo.objects.filter(empleado__cedula=cedula)
	context['solicitudes'] = Solicitud.objects.filter(empleado__cedula=cedula)
	#print(context['documentos'])
	
	#return render(request, 'main/index.html')
	return render(request, 'main/perfil.html', context)


def trabajo(request):
	context = {}
	context['logo'] = Estatico.objects.latest('telefono1')
	
	context['trabajos'] = Trabajo.objects.all()
	context['empleados'] = 		len(Empleado.objects.all())
	context['numeroTrabajos'] = len(context['trabajos'])
	context['hojas'] = 			len(Curriculum.objects.all())
	return render(request, 'main/trabajo.html', context)

def noticias(request):
	context = {}
	context['logo'] = Estatico.objects.latest('telefono1')
	
	context['noticias'] = Noticia.objects.all()
	return render(request, 'main/noticia.html', context)
	#return render(request, 'main/noticia1.html', context)