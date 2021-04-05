from django.db import models

# Create your models here.
from cap2.models import Etapa,Fase,Modulo
from ficha.models import CrearFicha


# class Arbol(models.Model):
#     componente = models.ForeignKey(Modulo, on_delete=models.CASCADE,default="")
#     fase = models.ForeignKey(Fase, on_delete=models.CASCADE,default="")
#     etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE,default="")
#     etapa_completo = models.BooleanField(verbose_name='Etapa completa')
#     created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
#     updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")




