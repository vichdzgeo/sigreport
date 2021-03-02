from django.db import models

# Create your models here.


class Maquina(models.Model):
    title =  models.CharField(max_length=1500,verbose_name = "Nombre de la máquina")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class Unidad(models.Model):
    title =  models.CharField(max_length=20,verbose_name = "Unidad de medida")
    description = models.TextField(max_length=1500,verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class EdificacionProvicional(models.Model):
    title =  models.CharField(max_length=1500,verbose_name = "Edificación en obras provisionales")
    description = models.TextField(max_length=1500,verbose_name="Descripción",blank = True)
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Edificacion provicional"
        verbose_name_plural = "Edificaciones provicionales"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class ActividadProvicional(models.Model):
    title =  models.CharField(max_length=1500,verbose_name = "Actividad")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Actividad provicional"
        verbose_name_plural = "Actividades provicionales"
        ordering = ["title"]
    
    def __str__(self):
        return self.title