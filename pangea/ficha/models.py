from django.db import models
from cap2.models import Modulo,Etapa,Fase
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from miscelanea.models import *
# Create your models here.


class CrearFicha(models.Model):
    #title = models.CharField(max_length=350,verbose_name="Nombre")
    componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    figura_loc = models.ImageField(default = 'null', verbose_name="Localización",upload_to="figuras_loc")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Ficha capítulo II"
        verbose_name_plural = "Fichas capítulo II"
        ordering = ["-created"]
    
    def __str__(self):
        return str(self.componente)

