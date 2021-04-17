from django.contrib import admin

# Register your models here.

from .models import *

class ImagenLocalizacionCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','fase')
    list_display = ('fase','etapa','componente')
    list_filter = ('fase','etapa','componente')

class CatFormAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','tipo','fase','etapa','componente')
    list_filter = ('tipo','fase','etapa','componente')


class SuperficieObrasCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','fase')
    list_display = ('edificaciones','superficie','componente','fase')

class FrecuenciaActividadesCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa')
    list_display = ('actividades','horas','componente','etapa','fase')


class ConsumoAguaCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa','unidad')
    list_display = ('tipo','unidad','cantidad','componente','etapa','fase')

class AguasResidualesCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa','unidad')
    list_display = ('tipo','unidad','cantidad','componente','etapa','fase')

class DescripcionGeneralAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa')
    list_display = ('componente','etapa','fase','content')


admin.site.register(CatForm,CatFormAdmin)
admin.site.register(ImagenLocalizacionC,ImagenLocalizacionCAdmin)
admin.site.register(FrecuenciaActividadesC,FrecuenciaActividadesCAdmin)
admin.site.register(SuperficieObrasC,SuperficieObrasCAdmin)
admin.site.register(ConsumoAguaC,ConsumoAguaCAdmin)
admin.site.register(AguasResidualesC,AguasResidualesCAdmin)
admin.site.register(DescripcionGeneral,DescripcionGeneralAdmin)

admin.site.site_header = 'Administrador Pangea'