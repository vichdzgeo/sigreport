# -*- coding: utf-8 -*-

from django import VERSION
from django.db import models
from cap2.models import Etapa,Fase,Modulo
from ficha.models import CrearFicha
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from miscelanea.models import *
#from mdeditor.fields import MDTextField
from ckeditor.widgets import CKEditorWidget
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
import pandas as pd 
from django.conf import settings
import os
import datetime 
def regresa_i(key,objetos):
    for i in objetos:
        if i.title == key:
            return i


def regresa(key,modelo):
    objetos = modelo.objects.all()
    for i in objetos:
        if i.title == key:
            return i.id

# Create your models here.


#### GENERALES #####

class FrecuenciaActividades(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")   
    actividades = models.ForeignKey(ListaActividades, on_delete=models.CASCADE,default="",verbose_name="Actividad")
    horas = models.IntegerField(verbose_name = "Jornadas/Etapa")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Frecuencia de actividades"
        verbose_name_plural = "Frecuencia de actividades"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.actividades)


class InsumosRequeridosAlmacenados(models.Model):
    OPT_ALM = (
        ('0%', '0%'),
        ('10%', '10%'),
        ('20%', '20%'),
        ('30%', '30%'),
        ('40%', '40%'),
        ('50%', '50%'),
        ('60%', '60%'),
        ('70%', '70%'),
        ('80%', '80%'),
        ('90%', '90%'),
        ('100%', '100%'),
        )
    #opt_alm_order = sorted(OPT_ALM)
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")   
    insumo = models.ForeignKey(InsumosLista, on_delete=models.CASCADE,default="",verbose_name="Insumo")
    cantidad = models.IntegerField(verbose_name = "cantidad",default=0)
    max_almacenado = models.CharField(max_length=10, choices=OPT_ALM,verbose_name = "Máximo almacenado",default='0%')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Insumos requeridos y almacenados"
        verbose_name_plural = "Insumos requeridos y almacenados"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.insumo)


class UsoSustanciasQuimicas(models.Model):
    OPT_ALM = (
        ('0%', '0%'),
        ('10%', '10%'),
        ('20%', '20%'),
        ('30%', '30%'),
        ('40%', '40%'),
        ('50%', '50%'),
        ('60%', '60%'),
        ('70%', '70%'),
        ('80%', '80%'),
        ('90%', '90%'),
        ('100%', '100%'),
        )
    #opt_alm_order = sorted(OPT_ALM)
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")   
    sustancia = models.ForeignKey(SustanciasQuimicasP, on_delete=models.CASCADE,default="",verbose_name="Insumo")
    cantidad = models.IntegerField(verbose_name = "cantidad",default=0)
    max_almacenado = models.CharField(max_length=10, choices=OPT_ALM,verbose_name = "Máximo almacenado",default='0%')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Uso de sustancias químicas peligrosas"
        verbose_name_plural = "Uso de sustancias químicas peligrosas"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.sustancia)

## Personal por etapa
class Personal(models.Model):
    OPT_ALM = (
        ('0%', '0%'),
        ('10%', '10%'),
        ('20%', '20%'),
        ('30%', '30%'),
        ('40%', '40%'),
        ('50%', '50%'),
        ('60%', '60%'),
        ('70%', '70%'),
        ('80%', '80%'),
        ('90%', '90%'),
        ('100%', '100%'),
        )
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    personal = models.ForeignKey(ListaTipoPersonal, on_delete=models.CASCADE,default="",verbose_name="Personal")
    cantidad_temporal = models.IntegerField(verbose_name = "Cantidad temporal",default=0)
    porcentaje_anual = models.CharField(max_length=10, choices=OPT_ALM,verbose_name = "Porcentaje del año",default='0%')
    cantidad_permanente = models.IntegerField(verbose_name = "Cantidad permanente",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"
        ordering = ['created']

    def __str__(self):
        return str(self.personal)


### Residuos sólidos por zonificación####  LISTO
class GeneracionResiduos(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    residuo = models.ForeignKey(ListaTipoResiduosSolidos, on_delete=models.CASCADE,default='',verbose_name="Tipo")
    cantidad = models.IntegerField(verbose_name = "Cantidad",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Generación de residuos sólidos"
        verbose_name_plural = "Generación de residuos sólidos"
        ordering = ['created']

    def __str__(self):
        return self.residuo.title
#### MAQUINARIA POR ETAPA   listo
        
class UsoMaquinaria(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    maquinaria = models.ForeignKey(Maquina, on_delete=models.CASCADE,default='', verbose_name="Tipo")
    horas = models.IntegerField(verbose_name = "Horas",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Uso de maquinaria"
        verbose_name_plural = "Uso de maquinaria"
        ordering = ['created']

    def __str__(self):
        return self.maquinaria
#### Vehiculos restringidos   PENDIENTE
class VehiculosRestrigidosZonificacion(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    tipov = models.ForeignKey(ListaTipoVehiculo,on_delete=models.CASCADE,verbose_name="Tipo de vehículo")
    restriccion = models.CharField(max_length=300,verbose_name="Condición")
    #cobertura = models.ForeignKey(ListaTiposCobertura,on_delete=models.CASCADE, default='')
    zonificacion = models.ForeignKey(ListaZonificacion,on_delete=models.CASCADE, default='',verbose_name="Zonificación")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "Selección de vehículos restringidos por zonificación"
        verbose_name_plural = "Selección de vehículos restringidos por zonificación"
        ordering = ['created']

    def __str__(self):
        return self.restriccion

## Aforo vehicular   LISTO
class AforoAlmacenamientoVehicular(models.Model):
    OPT_ALM = (
        ('n/a', 'n/a'),
        ('0%', '0%'),
        ('10%', '10%'),
        ('20%', '20%'),
        ('30%', '30%'),
        ('40%', '40%'),
        ('50%', '50%'),
        ('60%', '60%'),
        ('70%', '70%'),
        ('80%', '80%'),
        ('90%', '90%'),
        ('100%', '100%'),
        )
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    vehiculo = models.ForeignKey(VehiculoPorTipo, on_delete=models.CASCADE,default="",verbose_name="Vehículo")
    cantidad = models.IntegerField(verbose_name = "Cantidad",default=0)
    porcion_almacenada = models.CharField(max_length=10, choices=OPT_ALM,verbose_name = "Porción almacenada",default='0%')
    frec_operacion = models.IntegerField(verbose_name = "Frecuencia de operación (horas/año)",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Aforo y almacenamiento vehicular"
        verbose_name_plural = "Aforo y almacenamiento vehicular"
        ordering = ['created']

    def __str__(self):
        return str(self.vehiculo)

## EXTRACCIÓN AGUA
class ExtraccionAgua(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    pozo = models.CharField(max_length=300,verbose_name="Pozo")
    velocidad = models.IntegerField(verbose_name = "Velocidad L/s",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Velocidad de extracción de agua"
        verbose_name_plural = "Velocidad de extracción de agua"
        ordering = ['created']

    def __str__(self):
        return str(self.pozo)
### Formulario de Descripción de procesos constructivos
class DescripcionProcesosConstructivos(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default = None,blank=True,null=True)
    proceso_constructivo = models.ForeignKey(ListaProcesoConstructivo, on_delete=models.CASCADE,default="")
    contenido  = RichTextField(verbose_name="Descipción de proceso construcivo",default='')
    # created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    # updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Descripción de procesos constructivos"
        verbose_name_plural = "Descripción de procesos constructivos"
        ordering = ["-id"]
    
    def __str__(self):
        return str(self.id)
###  seleccion procesos const
class SeleccionProcesosConstructivos(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default = None,blank=True,null=True)
    procesos = models.ManyToManyField(ProcConstructivo, verbose_name="Procesos construcitivos")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")#     

    class Meta:
        verbose_name = "Selección de procesos constructivos"
        verbose_name_plural = "Selección de procesos constructivos"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.id)
### Sistemas constructivos seleccion
class SeleccionSistemasConstructivos(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default = None,blank=True,null=True)
    sistemas = models.ManyToManyField(SisConstructivo, verbose_name="Sistemas construcitivos")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")#     

    class Meta:
        verbose_name = "Selección de sistemas constructivos"
        verbose_name_plural = "Selección de sistemas constructivos"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.id)
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
        ("6", "Incluye obras provisionales semipermanentes"),
        ("7", "Incluye vialidades y senderos"),
        ("8", "Incluye actividades de alojamiento a visitantes (solo aplica para operación)"),
        ("9", "Incluye actividades de servicios, comerciales, recreativas o culturales (solo aplica en operación)"),
        ("10", "Incluye plantas de tratamiento y manejo de aguas residuales (solo aplica en mantenimiento)"),
        ("11", "Incluye planta potabilizadora (solo aplica en mantenimiento)"),

        )

    title = models.CharField(max_length=2500,verbose_name="Nombre del formulario")
    tipo = models.CharField(max_length=100,choices=TIPO_FORMULARIO,default="",verbose_name='tipo de formulario')
    tipo_c = models.CharField(max_length=10,choices=TIPO_COMPONENTE,default="1",verbose_name="tipo de componente al que aplica")
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="1")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default = None,blank=True,null=True)
    orden = models.IntegerField(verbose_name='orden',default=0)
    
    nurl = models.CharField(max_length=2500,verbose_name="nombre url",blank=True,default='')
    completo = models.BooleanField(default=False,verbose_name='completo')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    user = models.ForeignKey(User,verbose_name="Usuario",on_delete=models.PROTECT,default=None,null=True,blank=True)
    class Meta:
        verbose_name = "Formularios y catálogos"
        verbose_name_plural = "Formularios y catálogos"
        ordering = ["-created"]
       
    def __str__(self):
        return str(self.title)
## Frecuencia de actividades comerciales o de servicio
class FrecuenciaActCom(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    actividad = models.ForeignKey(ListaAct_scrc, on_delete=models.CASCADE,default="",verbose_name="Actividad comercial o de servicio")
    cantidad = models.IntegerField(verbose_name = "Jornadas/etapa",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Frecuencia de actividades de servicios, comerciales, recreativas o culturales"
        verbose_name_plural = "Frecuencia de actividades de servicios, comerciales, recreativas o culturales"
        ordering = ['created']

    def __str__(self):
        return str(self.personal)
## Ocupacion estimada de alojamiento
class OcupacionAloja(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    cobertura = models.ForeignKey(ListaTiposCobertura,on_delete=models.CASCADE, default='', verbose_name="Cobertura")
    oferta =models.CharField(max_length=500,verbose_name="Oferta de alojamiento")# (equivalencia en cuarto doble/2 personas)")
    huespedes_dia = models.IntegerField(verbose_name = "Número de huéspedes diarios",default=0)
    huespedes_etapa = models.IntegerField(verbose_name = "Número de huéspedes por etapa",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Ocupación estimada en componentes con alojamiento"
        verbose_name_plural = "Ocupación estimada en componentes con alojamiento"
        ordering = ['created']

    def __str__(self):
        return str(self.personal)

### AFORO VISITANTES
class AforoVisitantes(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    actividad = models.ForeignKey(ListActVisitantes,on_delete=models.CASCADE, default='',verbose_name="Actividad")
    maximo_etapa = models.IntegerField(verbose_name = "Máximo de visitantes por etapa",default=0)
    promedio_diario = models.IntegerField(verbose_name = "Promedio de visitantes diarios",default=0)
    maximo_diario = models.IntegerField(verbose_name = "Máximo de visitantes diarios",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Aforo máximo de visitantes por actividad"
        verbose_name_plural = "Aforo máximo de visitantes por actividad"
        ordering = ['created']

    def __str__(self):
        return str(self.actividad)




#### AFORO MAXIMO VEHICULAR
class AforoTipoVehiMaxDiario(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    vehiculo = models.ForeignKey(ListaTipoVehiculo, on_delete=models.CASCADE,default="",verbose_name="Tipo de vehículo")
    cantidad = models.IntegerField(verbose_name = "Cantidad de vehículos diariamente",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Aforo vehicular máximo diario por tipo de vehículo"
        verbose_name_plural = "Aforo vehicular máximo diario por tipo de vehículo"
        ordering = ['created']

    def __str__(self):
        return str(self.vehiculo)


#### AFORO  VEHICULAR total
class AforoTipoVehi(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    vehiculo = models.ForeignKey(ListaTipoVehiculo, on_delete=models.CASCADE,default="",verbose_name="Vehículo")
    cantidad = models.IntegerField(verbose_name = "Horas/etapa",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Aforo vehicular total por tipo de vehículo"
        verbose_name_plural = "Aforo vehicular total por tipo de vehículo"
        ordering = ['created']

    def __str__(self):
        return str(self.vehiculo)
#### PERSONAL TRANSPORTADO 
class PersonalTransportado(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    minimo = models.IntegerField(verbose_name = "Personal mínimo",default=0)
    maximo = models.IntegerField(verbose_name = "Personal máximo",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Personal transportado mínimo-máximo diario"
        verbose_name_plural = "Personal transportado mínimo-máximo"
        ordering = ['created']

    def __str__(self):
        return str(self.maximo)

## MANEJO DE SUSTANCIAS ESPECIALES
class ManejoSustanciasEspeciales(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    instalacion = models.ForeignKey(ListInsEsp, on_delete=models.CASCADE,verbose_name="Instalación especial")
    area = models.ForeignKey(ListaAreasManejoPeligrosas, on_delete=models.CASCADE,verbose_name="Área de manejo")
    actividad_especial = models.ForeignKey(ListaActInsEsp, on_delete=models.CASCADE,verbose_name="Tipo de actividades")
    manejo_sustancias = models.CharField(max_length=1500,verbose_name="Manejo de sustancias",default="No aplica")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Manejo de sustancias químicas peligrosas en instalaciones especiales"
        verbose_name_plural = "Manejo de sustancias químicas peligrosas en instalaciones especiales"
        ordering = ['created']

    def __str__(self):
        return str(self.area)
## CAPACIDAD DE ALMACENAMIENTO DE SUSTANCIAS 
class CapacidadAlmSustanciasEspeciales(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    instalacion = models.ForeignKey(ListInsEsp, on_delete=models.CASCADE,verbose_name="Instalación especial")
    sustancia = models.ForeignKey(SustanciasQuimicasP, on_delete=models.CASCADE,verbose_name="Sustancia química peligrosa")
    capacidad_alm = models.IntegerField(verbose_name="Capacidad de almacenamiento",default=0)
    recargas = models.IntegerField(verbose_name="Número de recargas al año",default=0)
    recargas_totales = models.IntegerField(verbose_name="Total de recargas en la etapa",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Capacidad de almacenamiento de sustancias químicas peligrosas en instalaciones especiales"
        verbose_name_plural = "Capacidad de almacenamiento de sustancias químicas peligrosas en instalaciones especiales"
        ordering = ['created']

    def __str__(self):
        return str(self.sustancia)
#### capacidad de almacenamiento
class CapacidadAlmResiduosEspeciales(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    instalacion = models.ForeignKey(ListInsEsp, on_delete=models.CASCADE,verbose_name="Instalación especial")
    residuo = models.ForeignKey(ResiduosPeligrosos, on_delete=models.CASCADE,verbose_name="Residuo peligroso")
    capacidad_veh = models.IntegerField(verbose_name="Capacidad de almacenamiento",default=0)
    viajes_anual = models.IntegerField(verbose_name="Número de viajes al año",default=0)
    viajes_totales = models.IntegerField(verbose_name="Total de viajes en la etapa",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Capacidad de almacenamiento de residuos peligrosos en instalaciones especiales"
        verbose_name_plural = "Capacidad de almacenamiento de residuos peligrosos en instalaciones especiales"
        ordering = ['created']

    def __str__(self):
        return str(self.residuo)

#### FRECUENCIA DE INGRESO DE SUSTANCIAS EN INSTALACIONES ESPECIALES
class FrecuenciaIngresoSusEspeciales(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    instalacion = models.ForeignKey(ListInsEsp, on_delete=models.CASCADE,verbose_name="Instalación especial")
    sustancia = models.ForeignKey(SustanciasQuimicasP, on_delete=models.CASCADE,verbose_name="Sustancia química peligrosa",default='')
    capacidad_veh = models.IntegerField(verbose_name="Capacidad de almacenamiento",default=0)
    viajes_anual = models.IntegerField(verbose_name="Número de viajes al año",default=0)
    viajes_totales = models.IntegerField(verbose_name="Total de viajes en la etapa",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Frecuencia de ingreso de sustancias peligrosas  en instalaciones especiales"
        verbose_name_plural = "Frecuencia de ingreso de sustancias peligrosas  en instalaciones especiales"
        ordering = ['created']

    def __str__(self):
        return str(self.sustancia)
#### FRECUENCIA DE INGRESO DE RESIDUOS EN INSTALACIONES ESPECIALES
class FrecuenciaIngresoResEspeciales(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    instalacion = models.ForeignKey(ListInsEsp, on_delete=models.CASCADE,verbose_name="Instalación especial")
    residuo = models.ForeignKey(ResiduosPeligrosos, on_delete=models.CASCADE,verbose_name="Residuo peligroso")
    capacidad_veh = models.IntegerField(verbose_name="Capacidad de almacenamiento",default=0)
    viajes_anual = models.IntegerField(verbose_name="Número de viajes al año",default=0)
    viajes_totales = models.IntegerField(verbose_name="Total de viajes en la etapa",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Frecuencia de ingreso de residuos peligrosos  en instalaciones especiales"
        verbose_name_plural = "Frecuencia de ingreso de residuos peligrosos  en instalaciones especiales"
        ordering = ['created']

    def __str__(self):
        return str(self.residuo)
### MAQUINARIA Y VIAJES PARA EL SUMINISTRO DE SUSTANCIAS
class MaquinariaViajesEsp(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    instalacion = models.ForeignKey(ListInsEsp, on_delete=models.CASCADE,verbose_name="Instalación especial")
    maquinaria = models.ForeignKey(Maquina, on_delete=models.CASCADE,verbose_name="Tipo de maquinaria")
    unidades = models.IntegerField(verbose_name="Número de unidades",default=0)
    viajes = models.IntegerField(verbose_name="Número de viajes por unidad",default=0)
    gasolina = models.IntegerField(verbose_name="Gasolina (L)",default=0)
    diesel = models.IntegerField(verbose_name="Diésel (L)",default=0)
    aceites = models.IntegerField(verbose_name="Aceites (L)",default=0)
    anticongelante = models.IntegerField(verbose_name="Anticongelante (L)",default=0)
    liq_frenos = models.IntegerField(verbose_name="Líquido de frenos (L)")
    lubricantes = models.IntegerField(verbose_name="Lubricantes (L)")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Maquinaria y viajes para el suministro de sustancias"
        verbose_name_plural = "Maquinaria y viajes para el suministro de sustancias"
        ordering = ["-created"]


    def __str__(self):
        return str(self.maquinaria)




## Tratamiento de aguas residuales
class TratamientoAguasResiduales(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    ptar = models.ForeignKey(ListaPTAR,on_delete=models.CASCADE,verbose_name="PTAR")
    cantidad = models.IntegerField(verbose_name = "L/s",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Tratamiento de aguas residuales por PTAR"
        verbose_name_plural = "Tratamiento de aguas residuales por PTAR"
        ordering = ['created']

    def __str__(self):
        return str(self.ptar)

# ###  INICIA FORMULARIOS PARA CONSTRUCCIÓN

class DatosGeneral(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')#regresa("Construcción",Fase))
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    sup_aprov_total = models.FloatField(verbose_name='Superficie aprovechable total (ha)')
    sup_edi = models.FloatField(verbose_name='Superficie edificable (ha)')
    sup_const_no_edi = models.FloatField(verbose_name='Superficie a construir no edificable (ha)')
    nivel_max = models.IntegerField(verbose_name='Niveles máximos construidos')
    zonificacion = models.CharField(max_length=30,verbose_name="Abreviaturas de las zonificaciones (separaras por comas)")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Datos generales del componente"
        verbose_name_plural = "Datos generales del componente"
        ordering = ["-created"]


    def __str__(self):
        return str(self.id)

class ImagenLocalizacionC(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')#regresa("Construcción",Fase))
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    image = models.ImageField(default = 'null', verbose_name="Figura",upload_to="figuras")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Imagen de localización y tipos de aprovechamiento - Construcción"
        verbose_name_plural = "Imagen de localización y tipos de aprovechamiento - Construcción"
        ordering = ["-created"]


    def __str__(self):
        return str(self.id)

class SuperficieObrasC(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    edificaciones = models.ForeignKey(EdificacionProvisional, on_delete=models.CASCADE,default="")
    superficie = models.IntegerField(verbose_name = "Superficie m²")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Superficie de obras o edificaciones provisionales temporales"
        verbose_name_plural = "Superficie de obras o edificaciones  provisionales temporales"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.edificaciones)

class FrecuenciaActividadesC(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")   
    actividades = models.ForeignKey(ActividadProvisional, on_delete=models.CASCADE,default="")
    horas = models.IntegerField(verbose_name = "Jornadas/Etapa")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Frecuencia de actividades de obras provisionales"
        verbose_name_plural = "Frecuencia de actividades de obras provisionales"
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
        verbose_name = "Consumo de agua"
        verbose_name_plural = "Consumo de agua"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.tipo)

class AguasResidualesC(models.Model):

    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")  
    tipo = models.ForeignKey(TipoAguaResidual, on_delete=models.CASCADE,default="")
    cantidad = models.PositiveIntegerField(verbose_name = "Cantidad en m³")
    unidad = models.CharField(max_length=10,default="m³")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Generación de aguas residuales"
        verbose_name_plural = "Generación de aguas residuales"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.tipo)

class DescripcionGeneral(models.Model):
    
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    duracion = models.PositiveIntegerField(verbose_name='Días de duración de las obras o actividades en la etapa',default=1)
    content = RichTextField(verbose_name="Descipción general del componente para esta etapa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Descripción general del componente para esta etapa"
        verbose_name_plural = "Descripción general del componente para esta etapa"
        ordering = ['componente', 'etapa']

    def __str__(self):
        return str(self.id)

##Descripción de las obras provisionales temporales
class DescripcionObrasTemporales(models.Model):
    
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    content = RichTextField(verbose_name="Descripción de las obras provisionales temporales del componente para esta etapa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Descripción de las obras provisionales temporales"
        verbose_name_plural = "Descripción de las obras provisionales temporales"
        ordering = ['componente', 'etapa']

    def __str__(self):
        return str(self.id)

##Descripción de la operación y mantenimiento para las obras provisionales temporales
class DescripcionOpeManObrasTemporales(models.Model):
    
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    content = RichTextField(verbose_name="Descripción de la operación y mantenimiento de las obras provisionales temporales del componente para esta etapa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Descripción de la operación y mantenimiento de las obras provisionales temporales"
        verbose_name_plural = "Descripción de la operación y mantenimiento de las obras provisionales temporales"
        ordering = ['componente', 'etapa']

    def __str__(self):
        return str(self.id)

class DescripcionGeneralFiguras(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    image = models.ImageField(default = 'null', verbose_name="Figura",upload_to="generales-fig")
    pie = models.CharField(max_length=300,verbose_name="pie de figura")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Figuras - Descripción general del componente - Construcción"
        verbose_name_plural = "Figuras - Descripción general del componente - Construcción"
        ordering = ["-created"]


    def __str__(self):
        return self.pie
class ListadoFloristicoC(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    flor = models.ForeignKey(ListadoFloristico, on_delete=models.CASCADE,default="")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Listado florístico en el módulo"
        verbose_name_plural = "Listado florístico en el módulo"
        ordering = ['flor']

    def __str__(self):
        return self.flor

class PersonalRequerido(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    personal = models.ForeignKey(ListaTipoPersonal, on_delete=models.CASCADE,default="")
    n_prot = models.IntegerField(verbose_name="Número de personal por zonificación Protección - PROT",default=0)
    n_rest = models.IntegerField(verbose_name="Número de personal por zonificación Uso restringido -  REST",default=0)
    n_apro = models.IntegerField(verbose_name="Número de personal por zonificación Uso Aprovechamiento controlado - APRO",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Personal requerido por zonificación"
        verbose_name_plural = "Personal requerido por zonificación"
        ordering = ['created']

    def __str__(self):
        return str(self.id)

#MaquinariaZonificacion
        
class MaquinariaZonificacion(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    maquinaria = models.ForeignKey(Maquina, on_delete=models.CASCADE,default='')
    n_prot = models.IntegerField(verbose_name="Número de horas por zonificación Protección - PROT",default=0)
    n_rest = models.IntegerField(verbose_name="Número de horas por zonificación Uso restringido -  REST",default=0)
    n_apro = models.IntegerField(verbose_name="Número de horas por zonificación Uso Aprovechamiento controlado - APRO",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Maquinaria por zonificación"
        verbose_name_plural = "Maquinaria por zonificación"
        ordering = ['created']

    def __str__(self):
        return self.maquinaria

class ObrasLinealesLongitudes(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    tipo = models.ForeignKey(ObrasLineales, on_delete=models.CASCADE,default='')
    longitud = models.FloatField(verbose_name="Longitud en Km",default=0.0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Longitud de obras lineales"
        verbose_name_plural = "Longitud de obras lineales"
        ordering = ['created']

    def __str__(self):
        return self.obra


class InsumosZonificacion(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    insumo = models.ForeignKey(InsumosLista, on_delete=models.CASCADE,default='')
    n_prot = models.IntegerField(verbose_name="Cantidad por zonificación Protección - PROT",default=0)
    n_rest = models.IntegerField(verbose_name="Cantidad por zonificación Uso restringido -  REST",default=0)
    n_apro = models.IntegerField(verbose_name="Cantidad por zonificación Uso Aprovechamiento controlado - APRO",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Insumos requeridos por zonificación"
        verbose_name_plural = "Insumos requeridos por zonificación"
        ordering = ['created']

    def __str__(self):
        return self.insumo

class MovimientoTierraZonificacion(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    tipo = models.ForeignKey(MovimientoTierra, on_delete=models.CASCADE,default='')
    n_prot = models.IntegerField(verbose_name="PROT",default=0)
    n_rest = models.IntegerField(verbose_name="REST",default=0)
    n_apro = models.IntegerField(verbose_name="APRO",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Desmonte, despalme, excavación y relleno por tipo de zonificación"
        verbose_name_plural = "Desmonte, despalme, excavación y relleno por tipo de zonificación"
        ordering = ['created']

    def __str__(self):
        return self.tipo
### Residuos sólidos por zonificación####
class ResiduosSolidosZonificacion(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default='')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    residuo = models.ForeignKey(ListaTipoResiduosSolidos, on_delete=models.CASCADE,default='')
    n_prot = models.IntegerField(verbose_name="PROT",default=0)
    n_rest = models.IntegerField(verbose_name="REST",default=0)
    n_apro = models.IntegerField(verbose_name="APRO",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Generación de residuos sólidos por zonificación"
        verbose_name_plural = "Generación de residuos sólidos por zonificación"
        ordering = ['created']

    def __str__(self):
        return self.residuo

def agrega_estructura():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'estructura_arbol_form3.txt')
    estructura = pd.read_csv(file_path, delimiter='\t',encoding='utf-8')
    estructura.sort_values(by='nombre',ascending=False)
    l_componentes  = Modulo.objects.all()
    l_etapas = Etapa.objects.all()
    l_fases = Fase.objects.all()

    for componente_i in l_componentes:
        print(componente_i.title,componente_i.etapas.all())
        for etapa_i in l_etapas:
            print("for etapa",componente_i.title,etapa_i)
            if etapa_i in componente_i.etapas.all():
                print("si esta")
                for index, row in estructura.iterrows():

                    if row['tipo_c']== 1 and componente_i.t_base == True: #and componente_i.t_aprov_edificable == False and componente_i.t_obras == False and componente_i.t_areas_verdes == False and componente_i.t_aprov_lineal == False:
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])

                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()
                    
                    elif row['tipo_c']== 2 and componente_i.t_base == True and componente_i.t_aprov_edificable == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])

                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 3 and componente_i.t_base == True and componente_i.t_obras == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 4 and componente_i.t_base == True and componente_i.t_areas_verdes == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 5 and componente_i.t_base == True and componente_i.t_aprov_lineal == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 6 and componente_i.t_base == True and componente_i.t_semipermanentes == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 7 and componente_i.t_base == True and componente_i.t_via_senderos == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 8 and componente_i.t_base == True and componente_i.t_hospedaje == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 9 and componente_i.t_base == True and componente_i.t_actividad == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()
                    elif row['tipo_c']== 10 and componente_i.t_base == True and componente_i.t_aguas == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

                    elif row['tipo_c']== 11 and componente_i.t_base == True and componente_i.t_plantas == True:  
                        nombre_f = row['nombre'] #0
                        tipo_f = str(row['tipo']) #1
                        tipoc_f = str(row['tipo_c']) #2
                        componente_f =componente_i  #3
                        fase_f =regresa_i(row['fase'],l_fases) #4
                        etapa_f = etapa_i  # 5
                        tag_url = str(row['tag-url'])
                        orden = int(row['orden'])
                        if not CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f).exists():

                            agrega_form = CatForm(
                                title = nombre_f,
                                tipo = tipo_f,
                                tipo_c = tipoc_f,
                                componente = componente_f,
                                fase = fase_f,
                                etapa =etapa_f,
                                nurl = tag_url,
                                orden=orden,
                                                )
                            agrega_form.save()

#@receiver(post_save,sender=Modulo)
# @receiver(m2m_changed,sender=Modulo.etapas)
# def ensure_model_exists(sender,instance,**kwargs):
#     print(instance.etapas.all())
#     if kwargs.get('created',True):
#         #Catform.objects.get_or_create(title=instance)
#         print("Se acaba de crear la estructura para un modulo")
#         agrega_estructura()

def models_etapas_changed(sender,**kwargs):
    agrega_estructura()
m2m_changed.connect(models_etapas_changed,sender=Modulo.etapas.through)

def models_modulo_changed(sender,**kwargs):
    i_componente = kwargs.get('instance',True)
    i_aprov_edificable =  kwargs.get('instance',True).t_aprov_edificable #2
    i_obras =  kwargs.get('instance',True).t_obras #3
    i_areas_verdes = kwargs.get('instance',True).t_areas_verdes #4
    i_aprov_lineal =  kwargs.get('instance',True).t_aprov_lineal #5
    i_semipermanentes =  kwargs.get('instance',True).t_semipermanentes #6
    i_via_senderos =  kwargs.get('instance',True).t_via_senderos #7
    i_hospedaje =  kwargs.get('instance',True).t_hospedaje #8
    i_actividad =  kwargs.get('instance',True).t_actividad #9
    i_aguas =  kwargs.get('instance',True).t_aguas #10
    i_plantas =  kwargs.get('instance',True).t_plantas #11

    lista_false =[]
    if i_aprov_edificable is False:
        lista_false.append("2")    
    if i_obras is False:
        lista_false.append("3")  
    if i_areas_verdes is False:
        lista_false.append("4")  
    if i_aprov_lineal is False:
        lista_false.append("5")
    if i_semipermanentes is False:
        lista_false.append("6")
    if i_via_senderos is False:
        lista_false.append("7")
    if i_hospedaje is False:
        lista_false.append("8")
    if i_actividad is False:
        lista_false.append("9")
    if i_aguas is False:
        lista_false.append("10")
    if i_plantas is False:
        lista_false.append("11")

          
    CatForm.objects.filter(componente=i_componente,tipo_c__in=lista_false).delete()
    agrega_estructura()
post_save.connect(models_modulo_changed,sender=Modulo)

