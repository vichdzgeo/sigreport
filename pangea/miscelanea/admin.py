from django.contrib import admin
from .models import *

# Register your models here.


class MaquinaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('tipo',)
    search_fields = ('tipo',)

class UnidadAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('title',)

class EdificacionProvisionalAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)

class ActividadProvisionalAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)


class TipoAguaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('tipo',)
    search_fields = ('tipo',)

class InsumosListaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)

class SustanciasQuimicasPAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)

class ListadoFloristicoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre','familia','especie','forma')
    search_fields = ('nombre',)

class ListaTipoPersonalAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('tipo',)
    search_fields = ('tipo',)

class SisConstructivoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('title',)

class SisFigurasAdmin(admin.ModelAdmin):
    list_display = ('sistema',)

admin.site.register(Maquina,MaquinaAdmin)
admin.site.register(Unidad,UnidadAdmin)
admin.site.register(EdificacionProvisional,EdificacionProvisionalAdmin)
admin.site.register(ActividadProvisional,ActividadProvisionalAdmin)

admin.site.register(TipoAgua,TipoAguaAdmin)
admin.site.register(InsumosLista,InsumosListaAdmin)
admin.site.register(SustanciasQuimicasP,SustanciasQuimicasPAdmin)
admin.site.register(ListadoFloristico,ListadoFloristicoAdmin)
admin.site.register(ListaTipoPersonal,ListaTipoPersonalAdmin)
admin.site.register(SisConstructivo,SisConstructivoAdmin)
admin.site.register(SisFiguras,SisFigurasAdmin)

admin.site.site_header = 'Administrador Pangea'