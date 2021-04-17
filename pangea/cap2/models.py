from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid
from django.conf import settings
# Create your models here.


class Modulo(models.Model):
    title = models.CharField(max_length=150,verbose_name="Componente")
    abreviatura = models.CharField(max_length=10,verbose_name="Abreviatura",default="")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    t_base = models.BooleanField(default=True,verbose_name="Base")
    t_aprov_edificable = models.BooleanField(default=False,verbose_name="Incluye aprovechamiento edificable")
    t_obras = models.BooleanField(default=False,verbose_name="Incluye obras provisionales temporales")
    t_areas_verdes = models.BooleanField(default=False,verbose_name="Incluye áreas verdes ornamentales")
    t_aprov_lineal = models.BooleanField(default=False,verbose_name="Incluye aprovechamiento líneal")

    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.title)



class Fase(models.Model):
    title = models.CharField(max_length=300,verbose_name="Fase")
    descripcion = models.TextField(max_length=1500,verbose_name="Descripción",blank=True,null=True)
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Fase"
        verbose_name_plural = "Fases"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.title)

class Etapa(models.Model):
    title = models.CharField(max_length=2,verbose_name="Etapa")
    inicio = models.PositiveIntegerField(verbose_name='Inicio',default=1)
    fin = models.PositiveIntegerField(verbose_name='fin',default=99)
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.title)



