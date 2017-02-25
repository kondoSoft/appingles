#encoding:utf-8

from django.db import models

class alumnos(models.Model):
	ciclo = models.CharField(max_length=10)
	grado = models.CharField(max_length=10, null=True)
	grupo = models.CharField(max_length=10, null=True)
	salon = models.CharField(max_length=10, null=True)
	nivel = models.CharField(max_length=30, null=True)
	semestre = models.CharField(null=True, max_length=10)
	matricula = models.CharField(max_length=10, verbose_name=u'Matrícula')
	lista = models.CharField(null=True, max_length=10)
	nombre = models.CharField(max_length=250)
	clasificacion_materia = models.CharField(max_length=25, verbose_name=u'Clasificación')
	numero_materia = models.CharField(null=True, max_length=10)
	nombre_materia = models.CharField(max_length=100, verbose_name=u'Nombre de la Materia')
	calif_sep = models.CharField(max_length=10, null=True, blank=True)
	calif_oct = models.CharField(max_length=10, null=True, blank=True)
	calif_nov = models.CharField(max_length=10, null=True, blank=True)
	calif_dic = models.CharField(max_length=10, null=True, blank=True)
	calif_ene = models.CharField(max_length=10, null=True, blank=True)
	calif_feb = models.CharField(max_length=10, null=True, blank=True)
	calif_mar = models.CharField(max_length=10, null=True, blank=True)
	calif_may = models.CharField(max_length=10, null=True, blank=True)
	calif_jun = models.CharField(max_length=10, null=True, blank=True)
	primer_trimestre = models.CharField(max_length=10, null=True, blank=True)
	promedio = models.CharField(max_length=10, null=True, blank=True)
	def __unicode__(self):
		return self.clasificacion_materia

class archivos_save(models.Model):
	archivo = models.FileField(upload_to='archivo', verbose_name=u'Subir txt')