from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import uuid
from django.conf import settings
# Create your models here.


class Etapa(models.Model):
    title = models.CharField(max_length=100,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title

class Fase(models.Model):

    title = models.CharField(max_length=100,verbose_name="Fase")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Fase"
        verbose_name_plural = "Fases"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title



class Componente(models.Model):
    
    title = models.CharField(max_length=500,verbose_name="Nombre")
    pie = models.TextField(max_length=2500,verbose_name="Descripción",blank=True,default='')


    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    #user = models.ForeignKey(User,verbose_name='usuario', on_delete=models.CASCADE)
    #imagen = models.ManyToManyField(Imagen,verbose_name = "Agregar imagen")
    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componentes"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title



class Imagen(models.Model):
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=300,verbose_name="Nombre")
    pie = models.TextField(max_length=1500,verbose_name="Pie de página")
    image = models.ImageField(default = 'null', verbose_name="Figura",upload_to="figuras")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"
        ordering = ["-created"]


    def __str__(self):
        return self.title

