from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

admin.site.site_header = 'Temco Administracion'


class ArchivoAdmin(admin.ModelAdmin):
	search_fields=['empleado__nombre']
	list_display = ('tipo', 'empleado')
	list_filter = ( 'fecha', 'tipo')
	class Meta:
		model = Archivo

class NoticiaAdmin(admin.ModelAdmin):
	list_display = ('titulo','fecha')
	list_filter = ('fecha',)

class TrabajoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'fecha')
	list_filter = ('tipo', 'fecha', )


class CurriculumAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'estado')
	list_filter = ('estado',)

class SolicitudAdmin(admin.ModelAdmin):
	search_fields=['empleado__nombre']
	list_display = ('tipo', 'empleado', 'estado')
	list_filter = ('estado', 'tipo', 'fecha')
	class Meta:
		model = Solicitud

# faltan filtros de strings para Empleado archivo-empleado solicitud empleado

admin.site.register(Estatico)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Trabajo, TrabajoAdmin)
admin.site.register(Empleado)
admin.site.register(Archivo, ArchivoAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Solicitud, SolicitudAdmin)




# Register your models here.
