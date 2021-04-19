from django.db import models
from cap2.models import Fase
from ckeditor.fields import RichTextField
# Create your models here.



class ObrasLineales(models.Model):
    tipo =  models.CharField(max_length=10,verbose_name = "Tipo de obra lineal")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de obras lineales"
        verbose_name_plural = "Lista de obras lineales"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

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

    tipo =  models.CharField(max_length=1500,verbose_name = "Tipo",default='')
    combustible = models.CharField(max_length=200, choices=opt_comb_order,verbose_name='Combustible/energía',default='Gasolina')
    hp = models.FloatField(verbose_name="hp",default=0.0)
    kwh = models.FloatField(verbose_name="KW-h",default=0.0)
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de maquinaría"
        verbose_name_plural = "Lista de maquinaría"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

class Unidad(models.Model):
    title =  models.CharField(max_length=10,verbose_name = "Unidad de medida")
    description = models.TextField(max_length=50,verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de unidades"
        verbose_name_plural = "Lista de unidades"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class EdificacionProvisional(models.Model):
    title =  models.CharField(max_length=1500,verbose_name = "Edificación en obras provisionales")
    description = models.TextField(max_length=1500,verbose_name="Descripción",blank = True)
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de obras o edificaciones provisionales temporales"
        verbose_name_plural = "Lista de obras o edificaciones provisionales temporales"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class ActividadProvisional(models.Model):
    title =  models.CharField(max_length=1500,verbose_name = "Actividad")
    
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de actividades provisionales"
        verbose_name_plural = "Lista de actividades provisionales"
        ordering = ["title"]
    
    def __str__(self):
        return self.title

class InsumosLista(models.Model):
    title = models.TextField(max_length=300,verbose_name = "Tipo")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,default="")
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
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,default="")
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
    
    tipo = models.CharField(max_length=100,verbose_name = "Tipo")
    descripcion = models.CharField(max_length=280,verbose_name = "Descripcion",default='')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de tipos de personal"
        verbose_name_plural = "Lista de tipos de personal"
        ordering = ["tipo"]
    def __str__(self):
        return self.tipo

class ListaSisConstructivo(models.Model):
    
    sistema = models.CharField(max_length=300,verbose_name = "Sistema constructivo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de sistemas constructivos"
        verbose_name_plural = "Lista de sistemas constructivos"
        ordering = ["sistema"]
    def __str__(self):
        return self.sistema

class DescripcionSisConstructivo(models.Model):
    
    sistema = models.ForeignKey(ListaSisConstructivo,on_delete=models.CASCADE,default="")
    content = RichTextField(verbose_name="Descipción del sistema constructivo", default="")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Descripción de sistemas constructivos"
        verbose_name_plural = "Descripción de sistemas constructivos"
        ordering = ["sistema"]
    def __str__(self):
        return self.sistema


class ListaSisConstructivoFiguras(models.Model):
    sistema = models.ForeignKey(ListaSisConstructivo,on_delete=models.CASCADE,default="")
    image = models.ImageField(default = 'null', verbose_name="Figura",upload_to="sistemasconstructivos-fig")
    pie = models.CharField(max_length=300,verbose_name="pie de figura")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    class Meta:
        verbose_name = "Figuras - Descripción del sistema constructivo"
        verbose_name_plural = "Figuras - Descripción del sistema constructivo"
        ordering = ["-created"]


    def __str__(self):
        return self.pie        

class ListaProcesoConstructivo(models.Model):
    proceso = models.CharField(max_length=280,verbose_name = "Proceso constructivo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de procesos constructivos"
        verbose_name_plural = "Lista de procesos constructivos"
        ordering = ["proceso"]
    def __str__(self):
        return self.proceso

class ListaTipoResiduos(models.Model):

    ESTADO_FISICO = (

        ("Sólido","Sólido"),
        ("Líquido", "Líquido"),
        ("Gaseoso", "Gaseoso"),
)
    tipo = models.CharField(max_length=100,verbose_name = "Tipo")
    corrosivo = models.BooleanField(default=False,verbose_name='Corrosivo')
    reactivo = models.BooleanField(default=False,verbose_name='Reactivo')
    explosivo = models.BooleanField(default=False,verbose_name='Explosivo')
    toxico = models.BooleanField(default=False,verbose_name='Toxico')
    inflamable = models.BooleanField(default=False,verbose_name='Inflamable')
    biologico = models.BooleanField(default=False,verbose_name='Biologico infeccioso')
    edo_fisico = models.CharField(max_length=15,choices=ESTADO_FISICO,default="Sólido",verbose_name='Estado físico')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de tipos de residuos"
        verbose_name_plural = "Lista de tipos de residuos"
        ordering = ["tipo"]
    def __str__(self):
        return self.tipo

class TipoAgua(models.Model):
    tipo = models.CharField(max_length=1500,verbose_name = "Tipo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de agua"
        verbose_name_plural = "Lista de tipos de agua"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

class TipoAguaResidual(models.Model):
    tipo = models.CharField(max_length=1500,verbose_name = "Tipo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de agua residuales"
        verbose_name_plural = "Lista de tipos de agua residuales"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo


class ListaTiposAprovechamiento(models.Model):
    tipo = models.CharField(max_length=100,verbose_name = "Tipo de aprovechamiento")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de aprovechamiento"
        verbose_name_plural = "Lista de tipos de aprovechamiento"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

class ListaTiposCobertura(models.Model):
    tipo = models.CharField(max_length=100,verbose_name = "Tipo de cobertura")
    abreviatura = models.CharField(max_length=10,verbose_name = "Abreviatura")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de cobertura y abreviaturas"
        verbose_name_plural = "Lista de tipos de cobertura y abreviaturas"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

class ListaZonificacion(models.Model):
    zona = models.CharField(max_length=100,verbose_name = "Zona")
    abreviatura = models.CharField(max_length=10,verbose_name = "Abreviatura")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de zonificación y abreviaturas"
        verbose_name_plural = "Lista de zonificación y abreviaturas"
        ordering = ["zona"]
    
    def __str__(self):
        return self.zona

class MovimientoTierra(models.Model):
    tipo = models.CharField(max_length=50,verbose_name = "Tipo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Catálogo de desmonte, despalme, excavación y relleno"
        verbose_name_plural = "Catálogo de desmonte, despalme, excavación y relleno"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

class ListaTiposConsEdif(models.Model):
    tipo = models.CharField(max_length=100,verbose_name = "Tipo de cobertura")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de construcción-edificación"
        verbose_name_plural = "Lista de tipos de construcción-edificación"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo