from django.db import models
from cap2.models import Etapa,Fase,Componente
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.


class SuperficieObras(models.Model):

    componente = models.ForeignKey(Componente, on_delete=models.CASCADE,default="")
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
    edificaciones =  models.CharField(max_length=500,verbose_name = "Edificaciones en obras provicionales")
    superficie = models.IntegerField(verbose_name = "Superficie m²")
    
    #published = models.DateTimeField(verbose_name = "Fecha de publicación",default = timezone.now)
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Superficie de obras provisionales temporales "
        verbose_name_plural = "Superficie de obras provisionales temporales"
        ordering = ["-created"]
    
    def __str__(self):
        return self.edificaciones