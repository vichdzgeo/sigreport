from django.db import models
from cap2.models import Fase
from ckeditor.fields import RichTextField
# Create your models here.

def regresa(key,modelo):
    objetos = modelo.objects.all()
    for i in objetos:
        if i.title == key:
            return i.id


###--- CATALOGOS GENERALES ---######

class Unidad(models.Model):
    title =  models.CharField(max_length=50,verbose_name = "Unidad de medida")
    description = models.TextField(max_length=50,verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de unidades"
        verbose_name_plural = "Lista de unidades"
        ordering = ["title"]
    
    def __str__(self):
        return self.title
class ListaTipoVehiculo(models.Model):

    tipo = models.CharField(max_length=1200,verbose_name = "Tipo de vehículo")
    descripcion = models.CharField(max_length=1500,verbose_name = "Descripción")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    
    
    class Meta:
        verbose_name = "Lista de tipo de vehículos"
        verbose_name_plural = "Lista de tipo de vehículos"
        ordering = ["tipo"]

    def __str__(self):
        return self.tipo
class VehiculoPorTipo(models.Model):
    OPT_COMBUSTIBLES = (
        ('Gasolina', 'Gasolina'),
        ('Diésel', 'Diésel'),
        ('Gas LP', 'Gas LP'),
        ('Gas natural', 'Gas natural'))
    opt_comb_order = sorted(OPT_COMBUSTIBLES)

    vehiculo = models.CharField(max_length=1200,verbose_name = "Vehículo")
    tipo = models.ForeignKey(ListaTipoVehiculo, verbose_name = "Tipo",on_delete=models.CASCADE,default="")
    combustible = models.CharField(max_length=200, choices=opt_comb_order,verbose_name='Combustible',default='Gasolina')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de vehículos por tipo"
        verbose_name_plural = "Lista de vehículos por tipo "
        ordering = ["vehiculo"]

    def __str__(self):
        return self.vehiculo
class ListInsEsp(models.Model):
    tipo = models.CharField(max_length=100,verbose_name = "Instalación especial")
    abreviatura = models.CharField(max_length=10,verbose_name = "Abreviatura")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de instalaciones especiales y abreviaturas"
        verbose_name_plural = "Lista de instalaciones especiales y abreviaturas"
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
class InsumosLista(models.Model):
    title = models.TextField(max_length=300,verbose_name = "Tipo")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase,on_delete=models.CASCADE,default=regresa("Construcción",Fase))
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de insumos"
        verbose_name_plural = "Lista de insumos"
        ordering = ["title"]
    
    def __str__(self):
        return self.title +' ('+self.unidad.title+')'
class SustanciasQuimicasP(models.Model):
    title = models.CharField(max_length=1500,verbose_name = "Tipo")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,default="")
    fase = models.ForeignKey(Fase,on_delete=models.PROTECT,default=regresa("Construcción",Fase))
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de sustancias químicas peligrosas requeridas y almacenadas"
        verbose_name_plural = "Lista de sustancias químicas peligrosas requeridas y almacenadas"
        ordering = ["title"]
    def __str__(self):
        return self.title +' ('+self.unidad.title+')'
class ListaTipoPersonal(models.Model):
    
    tipo = models.CharField(max_length=100,verbose_name = "Tipo")
    descripcion = models.CharField(max_length=280,verbose_name = "Descripcion",default='')
    fase = models.ForeignKey(Fase,on_delete=models.PROTECT,default=regresa("Construcción",Fase))
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de tipos de personal"
        verbose_name_plural = "Lista de tipos de personal"
        ordering = ["tipo"]
    def __str__(self):
        return self.tipo
class ListaTipoResiduosSolidos(models.Model):
    tipo = models.CharField(max_length=240,verbose_name = "Tipo")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,default="")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")


    class Meta:
        verbose_name = "Lista de tipos de residuos sólidos"
        verbose_name_plural = "Lista de tipos de residuos sólidos"
        ordering = ["tipo"]
    def __str__(self):
        return self.tipo +' ('+self.unidad.title+')'
class ListaTipoResiduos(models.Model):

    ESTADO_FISICO = (

        ("Sólido","Sólido"),
        ("Líquido", "Líquido"),
        ("Gaseoso", "Gaseoso"),)
    tipo = models.CharField(max_length=300,verbose_name = "Tipo")
    corrosivo = models.BooleanField(default=False,verbose_name='Corrosivo')
    reactivo = models.BooleanField(default=False,verbose_name='Reactivo')
    explosivo = models.BooleanField(default=False,verbose_name='Explosivo')
    toxico = models.BooleanField(default=False,verbose_name='Tóxico')
    inflamable = models.BooleanField(default=False,verbose_name='Inflamable')
    biologico = models.BooleanField(default=False,verbose_name='Biológico infeccioso')
    edo_fisico = models.CharField(max_length=15,choices=ESTADO_FISICO,default="Sólido",verbose_name='Estado físico')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de tipos de residuos tóxicos"
        verbose_name_plural = "Lista de tipos de residuos tóxicos"
        ordering = ["tipo"]
    def __str__(self):
        return self.tipo
class ListaActividades(models.Model):
    
    actividad = models.CharField(max_length=1500,verbose_name = "Actividad")
    fase = models.ForeignKey(Fase,on_delete=models.PROTECT,default=regresa("Construcción",Fase),verbose_name="Fase")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de actividades"
        verbose_name_plural = "Lista de actividades"
        ordering = ["actividad"]
    
    def __str__(self):
        return self.actividad
class ResiduosPeligrosos(models.Model):
    residuo = models.CharField(max_length=1500,verbose_name = "Residuo peligroso")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,default="",verbose_name="Unidad de medida")
    ins_especial = models.ForeignKey(ListInsEsp,on_delete=models.PROTECT,default="",verbose_name="Instalación especial")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de residuos peligrosos por instalación especial"
        verbose_name_plural = "Lista de residuos peligrosos por instalación especial"
        ordering = ["residuo"]
    def __str__(self):
        return self.residuo +' ('+self.unidad.title+')'
class ListaPTAR(models.Model):
    
    planta = models.CharField(max_length=1500,verbose_name = "Planta de tratamiento")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de plantas de tratamiento"
        verbose_name_plural = "Lista de plantas de tratamiento"
        ordering = ["planta"]
    
    def __str__(self):
        return self.planta

#### CATALOGOS DE CONSTRUCCIÓN
class ObrasLineales(models.Model):
    tipo =  models.CharField(max_length=280,verbose_name = "Tipo de obra lineal")
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
        ('Gas natural', 'Gas natural'),
        ('Electricidad', 'Electricidad'),
        ('Solar', 'Solar'),
        ('Eólica', 'Eólica'),
    )
    opt_comb_order = sorted(OPT_COMBUSTIBLES)

    tipo =  models.CharField(max_length=1500,verbose_name = "Tipo",default='')
    combustible = models.CharField(max_length=200, choices=opt_comb_order,verbose_name='Combustible/energía',default='Gasolina')
    hp = models.FloatField(verbose_name="hp",default=0.0)
    kwh = models.FloatField(verbose_name="KW-h",default=0.0)
    fase = models.ForeignKey(Fase,on_delete=models.PROTECT,default=regresa("Construcción",Fase))
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de maquinaría"
        verbose_name_plural = "Lista de maquinaría"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo
class EdificacionProvisional(models.Model):
    title =  models.CharField(max_length=1500,verbose_name = "Edificación en obras provisionales")
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
class ListadoFloristico(models.Model):


    SHIRT_SIZES = (
        ('Individuos', 'Individuos'),
        ('Semillas', 'Semillas'),
        ('Estacas', 'Estacas'),
        ('Esquejes', 'Esquejes'),
        ('Individuos o semillas', 'Individuos o semillas'),
        ('Individuos, semillas o estacas', 'Individuos, semillas o estacas'),
        ('Individuos, semillas o esquejes', 'Individuos, semillas o esquejes'),
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
class ProcConstructivo(models.Model):
    title = models.CharField(max_length=300,verbose_name = "Proceso constructivo")
    content = RichTextField(verbose_name="Descripción del proceso constructivo", default="")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Descripción de procesos constructivos"
        verbose_name_plural = "Descripción de procesos constructivos"
        ordering = ["title"]
    def __str__(self):
        return str(self.title)
class SisConstructivo(models.Model):
    title = models.CharField(max_length=300,verbose_name = "Sistema constructivo")
    #images = models.ManyToManyField(SisFiguras,on_delete=models.CASCADE,default="")
    content = RichTextField(verbose_name="Descipción del sistema constructivo", default="")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Descripción de sistemas constructivos"
        verbose_name_plural = "Descripción de sistemas constructivos"
        ordering = ["title"]
    def __str__(self):
        return str(self.title)
class SisFiguras(models.Model):
    sistema = models.ForeignKey(SisConstructivo,on_delete=models.CASCADE,default="")
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
    ### OBSOLETO##
    proceso = models.CharField(max_length=280,verbose_name = "Proceso constructivo")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")
    class Meta:
        verbose_name = "Lista de procesos constructivos"
        verbose_name_plural = "Lista de procesos constructivos"
        ordering = ["proceso"]
    def __str__(self):
        return self.proceso
class ListaTiposAprovechamiento(models.Model):
    ### A PARTIR DEL 4 DE OCTUBRE SE CAMBIA A LISTA DE TIPOS DE PROCESOS CONSTRUCTIVOS
    
    SUBTIPOS = (

        ("Edificable","Edificable"),
        ("No edificable", "No edificable"),
    )

    title = models.ForeignKey(ProcConstructivo,on_delete=models.CASCADE,verbose_name = "Tipo de proceso constructivo")
    subtipo = models.CharField(max_length=20,choices=SUBTIPOS,default="Edificable",verbose_name='Seleccionar el subtipo')
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de procesos constructivos"
        verbose_name_plural = "Lista de tipos de procesos constructivos"
        ordering = ["title"]
    
    def __str__(self):
        return self.title
class MovimientoTierra(models.Model):
    tipo = models.CharField(max_length=50,verbose_name = "Tipo")
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE,default="")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Catálogo de desmonte, despalme, excavación y relleno"
        verbose_name_plural = "Catálogo de desmonte, despalme, excavación y relleno"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo
class ListaTiposConsEdif(models.Model):
    ### DESCARTADO A PARTIR DEL 4 DE OCTUBRE 
    tipo = models.CharField(max_length=100,verbose_name = "Tipo de cobertura")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de tipos de construcción-edificación"
        verbose_name_plural = "Lista de tipos de construcción-edificación"
        ordering = ["tipo"]
    
    def __str__(self):
        return self.tipo

## Catálogos de la fase de operación  --- ####
class ListaAct_scrc(models.Model):
    
    actividad = models.CharField(max_length=1500,verbose_name = "Actividad")
    descripcion = models.CharField(max_length=1500,verbose_name = "Descripción", default="")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista y descripción de actividades de servicios, comerciales, recreativas o culturales"
        verbose_name_plural = "Lista y descripción de actividades de servicios, comerciales, recreativas o culturales"
        ordering = ["actividad"]
    
    def __str__(self):
        return self.actividad
class ListActVisitantes(models.Model):
    actividad = models.CharField(max_length=1500,verbose_name = "Actividad")
    fase = models.ForeignKey(Fase,on_delete=models.PROTECT,default=regresa("Operación",Fase))
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de actividades de visitantes"
        verbose_name_plural = "Lista de actividades de visitantes"
        ordering = ["actividad"]
    
    def __str__(self):
        return self.actividad
class ListaAreasManejoPeligrosas(models.Model):
    
    n_area = models.CharField(max_length=1500,verbose_name = "Área de manejo de sustancias peligrosas")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de áreas de manejo de sustancias peligrosas"
        verbose_name_plural = "Lista de áreas de manejo de sustancias peligrosas"
        ordering = ["n_area"]
    
    def __str__(self):
        return self.n_area
class ListaActInsEsp(models.Model):
    actividad = models.CharField(max_length=1500,verbose_name = "Actividad")
    created = models.DateTimeField(auto_now_add = True,verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "Lista de actividades en instalaciones especiales"
        verbose_name_plural = "Lista de actividades en instalaciones especiales"
    def __str__(self):
        return self.actividad
