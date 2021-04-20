# -*- coding: utf-8 -*-

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
from django.db.models.signals import post_save
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


### Sistemas constructivos seleccion
class SeleccionSistemasConstructivos(models.Model):
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default=None, null=True,blank=True)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default = None,blank=True,null=True)
    sistemas = models.ManyToManyField(DescripcionSisConstructivo, verbose_name="Sistemas construcitivos")
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
    class Meta:
        verbose_name = "Formularios y catálogos"
        verbose_name_plural = "Formularios y catálogos"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.title)



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
    duracion = models.TextField(max_length=30,verbose_name='Duración de las obras o actividades',default='')
    content = RichTextField(verbose_name="Descipción general del componente para esta etapa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Descripción general del componente para esta etapa"
        verbose_name_plural = "Descripción general del componente para esta etapa"
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
    cobertura = models.ForeignKey(ListaTiposCobertura, on_delete=models.CASCADE,default='')
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

#MaquinariaCobertura
        
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



def agrega_estructura():
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'estructura_arbol_form2.txt')
    estructura = pd.read_csv(file_path, delimiter='\t',encoding='utf-8')
    estructura.sort_values(by='nombre',ascending=False)
    l_componentes  = Modulo.objects.all()
    l_etapas = Etapa.objects.all()
    l_fases = Fase.objects.all()
    dicc_fases ={}

    
    for componente_i in l_componentes:
        for etapa_i in l_etapas:
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

                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

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
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

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
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

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
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

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
                    existe_form = CatForm.objects.filter(title=nombre_f,tipo =tipo_f,tipo_c=tipoc_f,componente=componente_f,fase=fase_f,etapa=etapa_f)
                    print (len(existe_form))
                    if len(existe_form)==0:

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
@receiver(post_save,sender=Modulo)
def ensure_model_exists(sender,instance,**kwargs):
    if kwargs.get('created',False) or  kwargs.get('created',False):
        #Catform.objects.get_or_create(title=instance)
        print("Se acaba de crear la estructura para un modulo")
        agrega_estructura()