from django import forms
from calificaciones.models import *
from django.forms.widgets import *
from django.contrib.admin import widgets

class ImportarForm(forms.ModelForm):
	class Meta:
		model = archivos_save
		fields=('archivo',)
		widgets = {
			'archivo': FileInput()
		}