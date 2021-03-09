from django.contrib import admin
from .models import CrearFicha

# Register your models here.
class CrearFichaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(CrearFicha,CrearFichaAdmin)