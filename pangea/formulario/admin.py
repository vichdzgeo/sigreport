from django.contrib import admin

# Register your models here.

from .models import SuperficieObras


class SuperficieObrasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('edificaciones','superficie','componente','etapa','fase')

admin.site.register(SuperficieObras,SuperficieObrasAdmin)
admin.site.site_header = 'Administrador Pangea'