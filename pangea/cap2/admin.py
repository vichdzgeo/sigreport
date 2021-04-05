from django.contrib import admin

from .models import (Etapa,
                    Fase,
                    Modulo)
# Register your models here.


class EtapaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','inicio','fin')

class FaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    

class ModuloAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('title',)



admin.site.register(Etapa,EtapaAdmin)
admin.site.register(Fase,FaseAdmin)
admin.site.register(Modulo,ModuloAdmin)
#admin.site.register(Imagen,ImagenAdmin)
admin.site.site_header = 'Administrador Pangea'

