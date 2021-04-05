from django.db import models

# Create your models here.


class Maquina(models.Model):
    OPT_COMBUSTIBLES = (
        ('Gasolina', 'Gasolina'),
        ('Diésel', 'Diésel'),
        ('Gas LP', 'Gas LP'),
        ('Gas natural', 'Gas naturals'),
        ('Electricidad', 'Electricidad'),
        ('Solar', 'Solar'),
        ('Eólica', 'Eólica'),
    )
    opt_comb_order = sorted(OPT_COMBUSTIBLES)

    tipo =  models.CharField(max_length=1500,verbose_name = "Tipo")
    combustible = models.CharField(max_length=200, choices=opt_comb_order,verbose_name='Combustible/energía')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de maquinaría"
        verbose_name_plural = "Lista de maquinaría"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

class Unidad(models.Model):
    title =  models.CharField(max_length=50,verbose_name = "Unidad de medida")
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
        verbose_name = "Lista de obras provisionales temporales"
        verbose_name_plural = "Lista de obras provisionales temporales"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class ActividadProvicional(models.Model):
    title =  models.CharField(max_length=1500,verbose_name = "Actividad")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Actividad provisional"
        verbose_name_plural = "Actividades provisionales"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class TipoAgua(models.Model):
    title = models.CharField(max_length=1500,verbose_name = "Tipo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de agua"
        verbose_name_plural = "Lista de tipos de agua"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class InsumosLista(models.Model):
    title = models.TextField(max_length=5000,verbose_name = "Insumo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de insumos de construcción"
        verbose_name_plural = "Lista de insumos de construcción"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class SustanciasQuimicasP(models.Model):
    title = models.CharField(max_length=1500,verbose_name = "Tipo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de sustancias químicas peligrosas requeridas y almacenadas"
        verbose_name_plural = "Lista de sustancias químicas peligrosas requeridas y almacenadas"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class ListadoFloristico(models.Model):


    SHIRT_SIZES = (
        ('Individuos', 'Individuos'),
        ('Semillas', 'Semillas'),
        ('Estacas', 'Estacas'),
        ('Individuos o semillas', 'Individuos o semillas'),
        ('Individuos, semillas o estacas', 'Individuos, semillas o estacas'),
    )
    familia = models.CharField(max_length=1500,verbose_name = "Familia")
    especie = models.CharField(max_length=1500,verbose_name = "Especie")
    nombre = models.CharField(max_length=1500,verbose_name = "Nombre común")
    forma = models.CharField(max_length=1500,verbose_name = "Forma biológica")
    rescate = models.CharField(max_length=1500, choices=SHIRT_SIZES,verbose_name='Criterios para rescate')

    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Listado florísico"
        verbose_name_plural = "Listado florísico"
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre

class ListaTipoPersonal(models.Model):
    
    tipo = models.CharField(max_length=1500,verbose_name = "Tipo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de tipos de personal"
        verbose_name_plural = "Lista de tipos de personal"
        ordering = ["tipo"]
    def __str__(self):
        return self.tipo

class ListaSisConstructivo(models.Model):
    
    sistema = models.CharField(max_length=1500,verbose_name = "Sistema constructivo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de sistemas constructivos"
        verbose_name_plural = "Lista de sistemas constructivos"
        ordering = ["sistema"]
    def __str__(self):
        return self.sistema