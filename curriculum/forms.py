# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render_to_response
from django.forms import ModelForm, TextInput, Textarea
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from lib.funciones import fecha_futura
from curriculum.models import Certificacion, Conocimiento, Competencia, ListaCompetencia, Educacion, Laboral, Competencia
from lugares.models import Institucion
import datetime

NIVELES_COMPTETENCIA = (
        ('experto','Experto'),
        ('alto','Alto'),
        ('medio','Medio'),
        ('basico',u'Básico'),
        ('nada','Nada'),
        )

class CompetenciaForm(forms.ModelForm):
    '''
    Formulario para el ingreso de Competencias en el panel administrativo
    '''
    class Meta:
        model = Competencia
        exclude = ('usuario',)

class ConocimientoForm(forms.ModelForm):
    '''
    Formulario general para el ingreso de Conocimientos
    '''
    class Meta:
        # Se determina cuál es el modelo al que va a referirse el formulario 
        model = Conocimiento
        exclude = ('usuario',)

class ConocimientoAdminForm(forms.ModelForm):
    '''
    Formulario general para el ingreso de Conocimientos en el admin
    '''
    class Meta:
        # Se determina cuál es el modelo al que va a referirse el formulario 
        model = Conocimiento

class CertificacionForm(forms.ModelForm):
    '''
    Formulario general para el ingreso de personas
    '''
    class Meta:
        # Se determina cuál es el modelo al que va a referirse el formulario 
        model = Certificacion
    def clean(self):
        '''
        Función para validaciones generales del modelo Curriculum
        '''
        fecha_inicio = self.data['fecha_inicio'] 
        fecha_fin = self.data['fecha_fin'] 
        # La fecha viene dada en string, por lo tanto se transforma a tipo fecha
        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%d/%m/%Y')
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%d/%m/%Y')
        # La fecha inicial no puede ser mayor a la final:
        if fecha_inicio > fecha_fin:
            raise forms.ValidationError(u'La fecha final no puede ser mayor ni igual al día de hoy')
        return self.cleaned_data

    def clean_fecha_inicio(self):
        '''
        Función para validar el campo de fecha inicio
        '''
        # Fecha actual
        fecha_actual = datetime.date.today()
        # Si fecha_actual es futura (función en lib/funciones.py)
        if fecha_futura(self.cleaned_data['fecha_inicio']):
            raise forms.ValidationError(u'La fecha de inicio no puede ser mayor ni igual al día de hoy')
        return self.cleaned_data['fecha_inicio']

class EducacionForm(forms.ModelForm):
    '''
    Formulario general para el ingreso de Conocimientos
    '''
    class Meta:
        # Se determina cuál es el modelo al que va a referirse el formulario 
        model = Educacion
        exclude = ('persona',)
        widgets = {
            'titulo': TextInput(attrs={'type':'text','required':'required','class':'form-control','placeholder':'Título obtenido'}),
            'carrera': TextInput(attrs={'type':'text','class':'form-control','placeholder':'Carrera estudiada'}),
            'fecha_inicio': TextInput(attrs={'type':'text','required':'required','class':'ink-datepicker','data-format':'dd/mm/yyyy','placeholder':'Fecha de inicio','id':'popupDatepicker'}),
            'fecha_fin': TextInput(attrs={'type':'text','required':'required','class':'ink-datepicker','data-format':'dd/mm/yyyy','placeholder':'Fecha de culminación','id':'popupDatepicker2'}),
        }

class LaboralForm(forms.ModelForm):
    '''
    Formulario general para el ingreso de Conocimientos
    '''
    class Meta:
        # Se determina cuál es el modelo al que va a referirse el formulario 
        model = Laboral
        exclude = ('usuario','trabajo_actual')
        widgets = {
            'empresa': TextInput(attrs={'type':'text','required':'required','placeholder':'Empresa en la que laboró'}),
            'sector': TextInput(attrs={'type':'text','placeholder':'Sector desempeñado'}),
            'telefono': TextInput(attrs={'type':'text','placeholder':'Número telefónico de trabajo'}),
            'cargo': TextInput(attrs={'type':'text','placeholder':'Cargo trabajado'}),
            'funcion': Textarea(attrs={'type':'text','placeholder':'Funciones desempeñadas'}),
            'fecha_inicio': TextInput(attrs={'type':'text','required':'required','class':'ink-datepicker','data-format':'dd/mm/yyyy','placeholder':'Fecha de inicio','id':'popupDatepicker'}),
            'fecha_fin': TextInput(attrs={'type':'text','required':'required','class':'ink-datepicker','data-format':'dd/mm/yyyy','placeholder':'Fecha de culminación','id':'popupDatepicker2'}),
            'retiro': TextInput(attrs={'type':'text','placeholder':'Razón de retiro'}),
            'direccion_empresa': Textarea(attrs={'type':'text','placeholder':'Dirección de la empresa'}),
        }
