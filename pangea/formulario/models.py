from django.db import models
from cap2.models import Etapa,Fase,Componente
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from miscelanea.models import EdificacionProvicional,ActividadProvicional,TipoAgua

# Create your models here.


class SuperficieObrasC(models.Model):

    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
    etapa = models.CharField(max_length=20,default="Construcción")
    #etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    edificaciones = models.ForeignKey(EdificacionProvicional, on_delete=models.CASCADE,default="")
    superficie = models.IntegerField(verbose_name = "Superficie m²")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Superficie de obras provisionales temporales - Construcción"
        verbose_name_plural = "Superficie de obras provisionales temporales  - Construcción"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.edificaciones)

class FrecuenciaActividadesC(models.Model):

    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
    etapa = models.CharField(max_length=20,default="Construcción")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    actividades = models.ForeignKey(ActividadProvicional, on_delete=models.CASCADE,default="")
    horas = models.IntegerField(verbose_name = "Jornadas/fase")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Frecuencia de actividades de obras provisionales - Construcción"
        verbose_name_plural = "Frecuencia de actividades de obras provisionales  - Construcción"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.actividades)

class ConsumoAguaC(models.Model):

    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
    etapa = models.CharField(max_length=20,default="Construcción")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    tipo = models.ForeignKey(TipoAgua, on_delete=models.CASCADE,default="")
    cantidad = models.PositiveIntegerField(verbose_name = "Cantidad en m³")
    unidad = models.CharField(max_length=10,default="m³")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Consumo de agua - Construcción"
        verbose_name_plural = "Consumo de agua - Construcción"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.tipo)

class AguasResidualesC(models.Model):

    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
    etapa = models.CharField(max_length=20,default="Construcción")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    tipo = models.ForeignKey(TipoAgua, on_delete=models.CASCADE,default="")
    cantidad = models.PositiveIntegerField(verbose_name = "Cantidad en m³")
    unidad = models.CharField(max_length=10,default="m³")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Generación de aguas residuales - Construcción"
        verbose_name_plural = "Generación de aguas residuales - Construcción"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.tipo)

# class Maquinaria(models.Model):

#     componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
#     etapa = models.CharField(max_length=20,default="Construcción")
#     fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
#     actividades = models.ForeignKey(ActividadProvicional, on_delete=models.CASCADE,default="")
#     horas = models.IntegerField(verbose_name = "Jornadas/fase")
#     created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
#     updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

#     class Meta:
#         verbose_name = "Frecuencia de actividades de obras provisionales - Construcción"
#         verbose_name_plural = "Frecuencia de actividades de obras provisionales  - Construcción"
#         ordering = ["-created"]
    
#     def __str__(self):
#         return str(self.actividades)