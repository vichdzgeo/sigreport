from django.contrib import admin

from .models import (Etapa,
                    Fase,
                    Componente,
                    Imagen)
# Register your models here.


class EtapaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class FaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ComponenteAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title',)
    search_fields = ('title',)
class ImagenAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','componente','etapa','fase')
    list_filter=('etapa','fase','componente')
    search_fields = ('title',)

admin.site.register(Etapa,EtapaAdmin)
admin.site.register(Fase,FaseAdmin)
admin.site.register(Componente,ComponenteAdmin)
admin.site.register(Imagen,ImagenAdmin)
admin.site.site_header = 'Administrador Pangea'

