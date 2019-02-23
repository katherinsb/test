from django.db import models
from django.contrib.auth.models import User


class Estatico(models.Model):
	titulo 		= models.CharField(max_length=45)
	mision 		= models.TextField()
	vision 		= models.TextField()
	correo 		= models.EmailField(max_length=45)
	telefono1 	= models.IntegerField()
	telefono2 	= models.IntegerField()
	ubicacion 	=  models.CharField(max_length=100)
	logo 		= models.ImageField(upload_to='media')
	horario 	= models.CharField(max_length=50)

	def __str__(self):
		return self.titulo
	



class Noticia(models.Model):
	titulo 		= models.CharField(max_length=50)
	fecha 		= models.DateTimeField('Fecha de Guardado')
	descripcion = models.TextField()
	enlace 		= models.CharField(max_length=500)

	def __str__(self):
		return self.titulo
	


class Trabajo(models.Model):
	HALF_TIME = 'Medio Tiempo'
	COMPLITE_TIME = 'Tiempo completo'
	CHOICES = (
		(HALF_TIME, 'Medio Tiempo'),
		(COMPLITE_TIME, 'Tiempo completo'),
	)

	titulo 		= models.CharField(max_length=70)
	subtitulo 	= models.CharField(max_length=70)
	descripcion = models.TextField()	
	tipo 		= models.CharField(max_length=20, choices=CHOICES, default=COMPLITE_TIME)
	salario 	= models.CharField(max_length=20)
	fecha 		= models.DateTimeField('Fecha de Guardado')
	direccion 	= models.CharField(max_length=70)
	imagen 		= models.ImageField(upload_to='media', default='no_image')

	def __str__(self):
		return self.titulo
	
	


class Empleado(models.Model):
	user 		= models.OneToOneField(User, on_delete=models.CASCADE) 
	nombre 		= models.CharField(max_length=70, unique=True)
	cedula 		= models.CharField(max_length=20, unique=True)
	correo 		= models.EmailField(unique=True)
	direccion 	= models.CharField(max_length=150, default='esta')
	telefono 	= models.CharField(max_length=10, default='1')
	curriculum 	= models.FileField(upload_to='media', default='no_file')
	imagen 		= models.ImageField(upload_to='media', default='no_image')

	def __str__(self): 
		return self.nombre 




class Archivo(models.Model):
	TIPO_UNO = 'Desprendible de pago'
	TIPO_DOS = 'Certificado de tabajo'
	TIPO_TRES = 'Certificado de EPS'
	TYPES = (
		(TIPO_UNO, 'Desprendible de pago'),
		(TIPO_DOS, 'Certificado de tabajo'),
		(TIPO_TRES, 'Certificado de EPS'),
	)

	empleado 	= models.ForeignKey(Empleado, on_delete=models.CASCADE)
	tipo 		= models.CharField(max_length=70, choices=TYPES, default=TIPO_UNO)
	documento 	= models.FileField(upload_to='media')
	fecha 		= models.DateTimeField('Fecha de Guardado')

	def __str__(self):
		return self.tipo + ' ' + str(self.empleado)




class Curriculum(models.Model):
	REVISADO = 'rv'
	SIN_REVISAR = 'SR'
	STATES = (
		(REVISADO,'Revisado'),
		(SIN_REVISAR, 'Sin revisar'),
	)

	documento 	= models.FileField(upload_to='media')
	nombre 		= models.CharField(max_length=70, unique=True)
	correo 		= models.EmailField()
	telefono1 	= models.IntegerField()
	estado 		= models.CharField(max_length=20, choices=STATES, default=SIN_REVISAR)
	texto 		= models.CharField(max_length=500, default='')

	def __str__(self):
		return self.nombre
	


class Solicitud(models.Model):
	TIPO_UNO = 'Desprendible de pago'
	TIPO_DOS = 'Certificado de tabajo'
	TIPO_TRES = 'Certificado de EPS'
	TYPES = (
		(TIPO_UNO, 'Desprendible de pago'),
		(TIPO_DOS, 'Certificado de tabajo'),
		(TIPO_TRES, 'Certificado de EPS'),
	)

	DISPONIBLE = 'Disponible'
	SIN_REVISAR = 'Sin revisar'
	EN_PROCESO = 'En proceso'
	STATES = (
		(DISPONIBLE,'Disponible'),
		(SIN_REVISAR, 'Sin revisar'),
		(EN_PROCESO, 'En proceso'),
	)


	empleado 	= models.ForeignKey(Empleado, on_delete=models.CASCADE)
	tipo 		= models.CharField(max_length=125, choices=TYPES)
	estado 		= models.CharField(max_length=20, choices=STATES, default=SIN_REVISAR)
	fecha 		= models.DateTimeField('Fecha de Guardado')	

	def __str__(self):
		return self.estado

	



