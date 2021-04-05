# -*- coding: utf-8 -*-

from django.db import models
from cap2.models import Etapa,Fase,Modulo
from ficha.models import CrearFicha
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from miscelanea.models import EdificacionProvicional,ActividadProvicional,TipoAgua


def regresa(key,modelo):
    objetos = modelo.objects.all()
    for i in objetos:
        if i.title == key:
            return i.id

# Create your models here.


class CatForm(models.Model):
    TIPO_FORMULARIO = (

        ("1","PNG"),
        ("2", "Catálogo"),
        ("3", "Catálogo de abreviaturas"),
        ("4", "Catálogo por fase"),
        ("5", "Formulario de datos"),
        ("6", "Formulario de datos y abreviaturas"),
        ("7", "Formulario de texto y figuras"),

        )
    TIPO_COMPONENTE = (
        ("1", "Base (todos)"),
        ("2", "Incluye aprovechamiento edificable"),
        ("3", "Incluye obras provisionales temporales"),
        ("4", "Incluye áreas verdes ornamentales"),
        ("5", "Incluye aprovechamiento lineal"),

        )

    title = models.CharField(max_length=2500,verbose_name="Nombre del formulario")
    tipo = models.CharField(max_length=100,choices=TIPO_FORMULARIO,default="",verbose_name='tipo de formulario')
    tipo_c = models.CharField(max_length=10,choices=TIPO_COMPONENTE,default="1",verbose_name="tipo de componente al que aplica")
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="1")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default = None,blank=True,null=True)
    
    url = models.CharField(max_length=2500,verbose_name="url",blank=True,default='')
    completo = models.BooleanField(default=False,verbose_name='completo')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Formularios y catálogos"
        verbose_name_plural = "Formularios y catálogos"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.title)



# ###  INICIA FORMULARIOS PARA CONSTRUCCIÓN

class ImagenLocalizacionC(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default=regresa("Construcción",Fase))
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=300,verbose_name="Nombre")
    image = models.ImageField(default = 'null', verbose_name="Figura",upload_to="figuras")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Imagen de localización y tipos de aprovechamiento - Construcción"
        verbose_name_plural = "Imagen de localización y tipos de aprovechamiento - Construcción"
        ordering = ["-created"]


    def __str__(self):
        return self.title

class SuperficieObrasC(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default=regresa("Construcción",Fase))
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
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

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default=regresa("Construcción",Fase))
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")   
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

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default=regresa("Construcción",Fase))
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")   
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

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default=regresa("Construcción",Fase))
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")  
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

# # class Maquinaria(models.Model):

# #     componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
# #     etapa = models.CharField(max_length=20,default="Construcción")
# #     fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
# #     actividades = models.ForeignKey(ActividadProvicional, on_delete=models.CASCADE,default="")
# #     horas = models.IntegerField(verbose_name = "Jornadas/fase")
# #     created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
# #     updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

# #     class Meta:
# #         verbose_name = "Frecuencia de actividades de obras provisionales - Construcción"
# #         verbose_name_plural = "Frecuencia de actividades de obras provisionales  - Construcción"
# #         ordering = ["-created"]
    
# #     def __str__(self):
# #         return str(self.actividades)

# ###  FINALIZA FORMULARIOS PARA CONSTRUCCIÓN