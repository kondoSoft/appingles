#encoding:utf-8
from django.shortcuts import render_to_response, redirect
from calificaciones.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.db.models import Q
from calificaciones.forms import *
import os
from django.db import connection, transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def buscar_matricula(request):
	q = None
	buscar = request.POST.get('buscar')
	clasifica = request.POST.get('clasifica')
	consulta = ''
	if buscar:
		consulta = alumnos.objects.filter(matricula=buscar, clasificacion_materia = 'ESPAÑOL')
		q = alumnos.objects.values('clasificacion_materia').distinct().exclude(clasificacion_materia='CLASIFICA')
	return render_to_response('lista_calificaciones.html',{'consulta':consulta,'buscar':buscar, 'q':q}, context_instance=RequestContext(request))

@xframe_options_exempt
def buscar_clasificacion(request, matricula, clasificacion):
	consulta = alumnos.objects.filter(matricula=matricula, clasificacion_materia=clasificacion)	
	q = alumnos.objects.values('clasificacion_materia').distinct().exclude(clasificacion_materia='CLASIFICA')
	return render_to_response('lista_calificaciones.html',{'consulta': consulta,'buscar':matricula,'q':q }, context_instance=RequestContext(request))

@login_required
def importar_archivo(request):
	if request.method == 'POST':
		archivoform = ImportarForm(request.POST, request.FILES)
		if archivoform.is_valid():
			archivo = archivoform.cleaned_data['archivo']
			a = archivos_save()
			a.archivo = archivo
			a.save()
			#messages.error(request, ERROR_MESSAGE)
			#cursor = connection.cursor()
			#cursor.execute("delete from calificaciones_alumnos;")
			#cursor.execute("COPY calificaciones_alumnos (ciclo, grado, grupo, salon, nivel, semestre, matricula, lista, nombre, clasificacion_materia, numero_materia, nombre_materia, calif_sep, calif_oct, calif_nov, calif_dic, calif_ene, calif_feb, calif_mar, calif_may, calif_jun, primer_trimestre, promedio) FROM '/home/developer/proyectos/appingles/appingles/carga/archivo/califica.txt';")
			os.system('/opt/sites/appingles/appingles/carga/archivo/insertar.sh')
			os.remove('/opt/sites/appingles/appingles/carga/archivo/califica.txt')
			messages.success(request, 'Se cargo exitosamente el archivo')
			#return redirect(buscar_matricula)
		else:
			messages.error(request, 'No ha cargado ningun archivo')
	else:
		archivoform = ImportarForm()
	return render_to_response('archivo.html',{'archivoform':archivoform}, context_instance=RequestContext(request))
