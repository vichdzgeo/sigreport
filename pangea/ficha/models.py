from django.db import models
from cap2.models import Etapa,Fase,Componente
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from miscelanea.models import EdificacionProvicional,ActividadProvicional
# Create your models here.


class CrearFicha(models.Model):
    #title = models.CharField(max_length=350,verbose_name="Nombre")
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    content =  RichTextField(verbose_name = "Descripción general del componente para esta fase")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Ficha capítulo II"
        verbose_name_plural = "Fichas capítulo II"
        ordering = ["-created"]
    
    def __str__(self):
        return self.componente