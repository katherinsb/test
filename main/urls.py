from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, re_path


from . import views

app_name= 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    #path('usuario', views.usuario, name='usuario'),
    path('perfil', views.perfil, name='perfil'),
    path('trabajo', views.trabajo, name='trabajo'),
    path('noticias', views.noticias, name='noticias')
    

]

