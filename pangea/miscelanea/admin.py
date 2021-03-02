from django.contrib import admin
from .models import *

# Register your models here.


class MaquinaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)

class UnidadAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)

class EdificacionProvicionalAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)

class ActividadProvicionalAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('tittle',)

admin.site.register(Maquina,MaquinaAdmin)
admin.site.register(Unidad,UnidadAdmin)
admin.site.register(EdificacionProvicional,EdificacionProvicionalAdmin)
admin.site.register(ActividadProvicional,ActividadProvicionalAdmin)
admin.site.site_header = 'Administrador Pangea'