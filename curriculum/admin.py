from django.contrib import admin
from curriculum.models import *
from curriculum.forms import (
        CertificacionForm, ConocimientoForm,
        CompetenciaForm, Educacion,
        ConocimientoAdminForm)

admin.site.register(Certificacion)


class ConocimientoAdmin(admin.ModelAdmin):
    form = ConocimientoAdminForm
admin.site.register(Conocimiento, ConocimientoAdmin)


class IdiomaAdmin(admin.ModelAdmin):
    search_fields = ('idioma',)
    list_display = ('persona', 'idioma',
            'nivel_leido', 'nivel_escrito', 'nivel_hablado')
    list_filter = ('idioma',)
admin.site.register(Idioma, IdiomaAdmin)


class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'puntaje')
    list_filter = ('tipo',)
    ordering = ('tipo__listacompetencia__tipo', 'id')
admin.site.register(Competencia, CompetenciaAdmin)


class TipoCompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puntaje_maximo')
    ordering = ('id',)
admin.site.register(TipoCompetencia, TipoCompetenciaAdmin)


class ListaCompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'puntaje_maximo')
    list_filter = ('tipo',)
    ordering = ('tipo', 'id')
admin.site.register(ListaCompetencia, ListaCompetenciaAdmin)


class CitaAdmin(admin.ModelAdmin):
    list_display = (
            'usuario',
            'primera_fecha',
            'segunda_fecha',
            'tercera_fecha',
            'cita_fijada')
admin.site.register(Cita, CitaAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display = (
            'usuario',
            'titulo',
            'estado',
            'fecha_inicio',
            'fecha_fin',
            'horas')

    list_filter = (
            'fecha_inicio',
            'fecha_fin')
admin.site.register(Curso, CursoAdmin)
class AprobacionAdmin(admin.ModelAdmin):
    list_display = (
        'entrevista_aprobatoria',
        'entrevista_maxima',
        'evaluacion_aprobatoria',
        'evaluacion_maxima',
            )
admin.site.register(Aprobacion, AprobacionAdmin)
admin.site.register(Educacion)
admin.site.register(TipoEducacion)
admin.site.register(Laboral)
admin.site.register(ListaIdiomas)
admin.site.register(Evaluacion)
