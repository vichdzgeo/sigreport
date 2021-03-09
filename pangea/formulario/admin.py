from django.contrib import admin

# Register your models here.

from .models import (SuperficieObrasC,
                    FrecuenciaActividadesC,
                    ConsumoAguaC,
                    AguasResidualesC,)


class SuperficieObrasCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa')
    list_display = ('edificaciones','superficie','componente','etapa','fase')

class FrecuenciaActividadesCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa')
    list_display = ('actividades','horas','componente','etapa','fase')


class ConsumoAguaCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa','unidad')
    list_display = ('tipo','unidad','cantidad','componente','etapa','fase')

class AguasResidualesCAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','etapa','unidad')
    list_display = ('tipo','unidad','cantidad','componente','etapa','fase')


admin.site.register(FrecuenciaActividadesC,FrecuenciaActividadesCAdmin)
admin.site.register(SuperficieObrasC,SuperficieObrasCAdmin)
admin.site.register(ConsumoAguaC,ConsumoAguaCAdmin)
admin.site.register(AguasResidualesC,AguasResidualesCAdmin)

admin.site.site_header = 'Administrador Pangea'