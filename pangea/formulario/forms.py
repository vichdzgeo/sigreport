from django import forms 
from .models import *
from cap2.models import Modulo,Fase,Etapa
from ckeditor.widgets import CKEditorWidget
from miscelanea.models import InsumosLista
def regresa_instancia_title(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.title == key:
            return i



## GENERALES #####################

class FrecuenciaActividadesForm(forms.ModelForm):

    class Meta:
        model = FrecuenciaActividades
        fields = ['actividades','horas']
        
        widgets = {
            'actividades': forms.Select(attrs={'class':'form-control'}),
            'horas': forms.NumberInput(attrs={'class':'form-control'}),           
        }

        labels ={'actividades':'Seleccionar una actividad',
        'horas':'Ingresar Jornadas/Etapa',}
class InsumosRequeridosAlmacenadosForm(forms.ModelForm):

    class Meta:
        model = InsumosRequeridosAlmacenados
        fields = ['insumo','cantidad','max_almacenado']
        
        widgets = {
            'insumo': forms.Select(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),           
            'max_almacenado': forms.Select(attrs={'class':'form-control'}),
        }

        labels ={'insumo':'Seleccionar un insumo',
        'cantidad':'Ingresar la cantidad',
        'max_almacenado':'Seleccionar Máximo almacenado'}
class UsoSustanciasQuimicasForm(forms.ModelForm):

    class Meta:
        model = UsoSustanciasQuimicas
        fields = ['sustancia','cantidad','max_almacenado']
        
        widgets = {
            'sustancia': forms.Select(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),           
            'max_almacenado': forms.Select(attrs={'class':'form-control'}),
        }

        labels ={'sustancia':'Seleccionar una sustancia',
        'cantidad':'Ingresar la cantidad',
        'max_almacenado':'Seleccionar Máximo almacenado'}
class PersonalForm(forms.ModelForm):

    class Meta:
        model = Personal
        fields = ['personal','cantidad_temporal','porcentaje_anual','cantidad_permanente']
        
        widgets = {
            'personal': forms.Select(attrs={'class':'form-control'}),
            'cantidad_temporal': forms.NumberInput(attrs={'class':'form-control'}),  
            'porcentaje_anual': forms.Select(attrs={'class':'form-control'}),
            'cantidad_permanente': forms.NumberInput(attrs={'class':'form-control'}),           
        }

        labels ={'personal':'Seleccionar tipo de personal',
        'cantidad_temporal':'Ingresar cantidad temporal',
        'porcentaje_anual':'Seleccionar porcentaje del año',
        'cantidad_permanente':'Ingresar cantidad permanente',}


####################################

class SeleccionProcesosConstructivosForm(forms.ModelForm):
    class Meta:
        model = SeleccionProcesosConstructivos
        fields = ['procesos',]
        exclude =('created','updated')
        widgets = {

            'procesos': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

        labels ={
            'procesos':'Seleccionar procesos constructivos'
        }
class SeleccionSistemasConstructivosForm(forms.ModelForm):
    class Meta:
        model = SeleccionSistemasConstructivos
        fields = ['sistemas',]
        exclude =('created','updated')
        widgets = {

            'sistemas': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

        labels ={
            'sistemas':'Seleccionar sistemas constructivos'
        }
class DatosGeneralForm(forms.ModelForm):
    class Meta:
        model = DatosGeneral
        fields =  ['sup_aprov_total','sup_edi','sup_const_no_edi','nivel_max','zonificacion']

        widgets = { 
            # 'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            # 'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            # 'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'sup_aprov_total': forms.NumberInput(attrs={'class':'form-control'}),
            'sup_edi': forms.NumberInput(attrs={'class':'form-control'}),
            'sup_const_no_edi': forms.NumberInput(attrs={'class':'form-control'}),
            'nivel_max': forms.NumberInput(attrs={'class':'form-control'}),
            'zonificacion': forms.TextInput(attrs={'class':'form-control'})
        }

        labels={'zonificacion':"Abreviaturas de las zonificaciones (separadas por comas)"}
    def clean_componente_fase_etapa(self):
        componente = self.cleaned_data.get("componente")
        fase = self.cleaned_data.get("fase")
        etapa = self.cleaned_data.get("etapa")
        if 'componente' in self.changed_data and 'fase' in self.changed_data and 'etapa' in self.changed_data:
            if DatosGeneral.objects.fiter(componente=componente, fase=fase,etapa=etapa).exits():
                raise form.ValidationError("Esta descripción general para este componente ya fue registrada")
            return componente,fase,etapa
class FormLocalizacionC(forms.ModelForm):

    class Meta:
        model = ImagenLocalizacionC
        fields = ['image',]
        
        widgets = {
            # 'componente': forms.Select(attrs={'class':'form-control'}),
            # 'fase': forms.Select(attrs={'class':'form-control'}),
            # 'etapa': forms.Select(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),           
        }
class FormCatForm(forms.ModelForm):

    class Meta:
        model = CatForm
        fields = ['title','completo',]
        #fields = ['title','componente','fase','etapa','completo']
        
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control','readonly':'readonly',}),
            # 'componente': forms.Select(attrs={'class':'form-control','readonly':'readonly','disabled':'disabled'}),
            # 'fase': forms.Select(attrs={'class':'form-control','readonly':'readonly','disabled':'disabled'}),
            # 'etapa': forms.Select(attrs={'class':'form-control','readonly':'readonly','disabled':'disabled'}),
            'completo': forms.CheckboxInput(attrs={'class':'form-control ml-2'}),
            }

        labels = {
            'completo':'Marcar como completo y verificado / Desactivar para pendiente',

        }
class FrecuenciaActividadesCForm(forms.ModelForm):

    class Meta:
        model = FrecuenciaActividadesC
        fields = ['actividades','horas']
        #fields = ['actividades','horas']
        
        widgets = {
            'actividades': forms.Select(attrs={'class':'form-control'}),
            'horas': forms.NumberInput(attrs={'class':'form-control'}),           
        }
class DescripcionGeneralForm(forms.ModelForm):
    class Meta:
        model = DescripcionGeneral
        fields = ['duracion','content']
     
        widgets = {
            'duracion': forms.TextInput(attrs={'class':'form-control',}),        
            'content': forms.TextInput(attrs={'class':'form-control',}),        
        }

        labels={
            'content':'Agregar la descripción'
        }
class DescripcionObrasTemporalesForm(forms.ModelForm):
    class Meta:
        model = DescripcionObrasTemporales
        fields = ['content']
     
        widgets = {
           'content': forms.TextInput(attrs={'class':'form-control',}),        
        }

        labels={
            'content':'Agregar la descripción'
        }
class DescripcionOpeManObrasTemporalesForm(forms.ModelForm):
    class Meta:
        model = DescripcionOpeManObrasTemporales
        fields = ['content']
     
        widgets = {
           'content': forms.TextInput(attrs={'class':'form-control',}),        
        }

        labels={
            'content':'Agregar la descripción'
        }
class DescripcionGeneralFigurasForm(forms.ModelForm):

    class Meta:
        model = DescripcionGeneralFiguras
        fields = ['image','pie']
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'pie': forms.TextInput(attrs={'class':'form-control'}),         
        }
class SuperficieObrasCForm(forms.ModelForm):
    class Meta:
        model = SuperficieObrasC
        fields = ['edificaciones','superficie']
     
        widgets = {

            'edificaciones': forms.Select(attrs={'class':'form-control'}),
            'superficie': forms.NumberInput(attrs={'class':'form-control'}),                   
        }

        labels={
            'edificaciones':'Seleccionar obra o edificación provisional temporal',
            'superficie':'Agregar la superficie en m²'
        }
class ConsumoAguaCForm(forms.ModelForm):
    class Meta:
        model = ConsumoAguaC
        fields = ['tipo','unidad','cantidad']
     
        widgets = {
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'unidad': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),                   
        }

        labels={
            'tipo':'Seleccionar el tipo de agua',
            'cantidad':'Agregar la cantidad en m³'
        }
class AguasResidualesCForm(forms.ModelForm):
    class Meta:
        model = AguasResidualesC
        fields = ['tipo','unidad','cantidad']
     
        widgets = {
            
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'unidad': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),                   
        }

        labels={
            'tipo':'Seleccionar el tipo de agua',
            'cantidad':'Agregar la cantidad en m³'
        }
class ListadoFloristicoCForm(forms.ModelForm):
    class Meta:
        model = ListadoFloristicoC
        fields = ['flor']
     
        widgets = {
            'flor': forms.Select(attrs={'class':'form-control'}),
            
        }

        labels={
            'flor':'Seleccionar el tipo de especie',

        }
class PersonalRequeridoForm(forms.ModelForm):
    class Meta:
        model = PersonalRequerido
        fields = ['personal','n_prot','n_rest','n_apro']
     
        widgets = {
            'personal': forms.Select(attrs={'class':'form-control'}),
            'n_prot': forms.NumberInput(attrs={'class':'form-control'}),
            'n_rest': forms.NumberInput(attrs={'class':'form-control'}),
            'n_apro': forms.NumberInput(attrs={'class':'form-control'}),
            
        }

        labels={
            'personal':'Seleccionar el tipo de personal',
            'n_prot':'PROT',
            'n_rest':'REST',
            'n_apro':'APRO',

        }
class InsumosZonificacionForm(forms.ModelForm):

    class Meta:
        model = InsumosZonificacion
        

        fields = ['insumo','n_prot','n_rest','n_apro']
        widgets = {

            'insumo': forms.Select(attrs={'class':'form-control'}),
            'n_prot': forms.NumberInput(attrs={'class':'form-control'}),
            'n_rest': forms.NumberInput(attrs={'class':'form-control'}),
            'n_apro': forms.NumberInput(attrs={'class':'form-control'}),
        }

        labels={
            'insumo':'Seleccionar el insumo',
            'n_prot':'PROT',
            'n_rest':'REST',
            'n_apro':'APRO',

        }
class MaquinariaZonificacionForm(forms.ModelForm):
    class Meta:
        model = MaquinariaZonificacion
        fields = ['maquinaria','n_prot','n_rest','n_apro']
     
        widgets = {

            'maquinaria': forms.Select(attrs={'class':'form-control'}),
            'n_prot': forms.NumberInput(attrs={'class':'form-control'}),
            'n_rest': forms.NumberInput(attrs={'class':'form-control'}),
            'n_apro': forms.NumberInput(attrs={'class':'form-control'}),
            
        }

        labels={
            'maquinaria':'Seleccionar el tipo de maquinaria',
            'n_prot':'PROT',
            'n_rest':'REST',
            'n_apro':'APRO',


        }
class MovimientoTierraZonificacionForm(forms.ModelForm):
    class Meta:
        model = MovimientoTierraZonificacion
        fields = ['tipo','n_prot','n_rest','n_apro']
     
        widgets = {

            'tipo': forms.Select(attrs={'class':'form-control'}),
            'n_prot': forms.NumberInput(attrs={'class':'form-control'}),
            'n_rest': forms.NumberInput(attrs={'class':'form-control'}),
            'n_apro': forms.NumberInput(attrs={'class':'form-control'}),
            
        }

        labels={
            'tipo':'Seleccionar tipo',
            'n_prot':'PROT',
            'n_rest':'REST',
            'n_apro':'APRO',


        }    
class ResiduosSolidosZonificacionForm(forms.ModelForm):
    class Meta:
        model = ResiduosSolidosZonificacion
        fields = ['residuo','n_prot','n_rest','n_apro']
     
        widgets = {

            'residuo': forms.Select(attrs={'class':'form-control'}),
            'n_prot': forms.NumberInput(attrs={'class':'form-control'}),
            'n_rest': forms.NumberInput(attrs={'class':'form-control'}),
            'n_apro': forms.NumberInput(attrs={'class':'form-control'}),
            
        }

        labels={
            'tipo':'Seleccionar tipo',
            'n_prot':'PROT',
            'n_rest':'REST',
            'n_apro':'APRO',


        }
class ObrasLinealesLongitudesForm(forms.ModelForm):
    class Meta:
        model = ObrasLinealesLongitudes
        fields = ['tipo','longitud']
     
        widgets = {
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'longitud': forms.NumberInput(attrs={'class':'form-control'}),                   
        }

        labels={
            'tipo':'Seleccionar obra lineal',
            'longitud':'Agregar longitud en Km'
        }
class VehiculosRestrigidosZonificacionForm(forms.ModelForm):
    class Meta:
        model = VehiculosRestrigidosZonificacion
        fields = ['zonificacion','tipov','restriccion']
     
        widgets = {
            'zonificacion': forms.Select(attrs={'class':'form-control'}),
            'tipov': forms.Select(attrs={'class':'form-control'}),
            'restriccion':forms.TextInput(attrs={'class':'form-control'}),

            
        }

        labels={
            'zonificación':'Seleccionar zonificación',
            'tipov':'Seleccionar tipo de vehículo',
            'restriccion':'Ingresar condición / restricción',
        }
class UsoMaquinariaForm(forms.ModelForm):
    class Meta:
        model = UsoMaquinaria
        fields = ['maquinaria','horas']
     
        widgets = {
            'maquinaria': forms.Select(attrs={'class':'form-control'}),
            'horas':forms.NumberInput(attrs={'class':'form-control'}),

            
        }

        labels={
            'maquinaria':'Seleccionar maquinaria',
            'horas':'Ingresar horas',
        }
class GeneracionResiduosForm(forms.ModelForm):
    class Meta:
        model = GeneracionResiduos
        fields = ['residuo','cantidad']
     
        widgets = {
            'residuo': forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),

            
        }

        labels={
            'residuo':'Seleccionar residuo',
            'cantidad':'Ingresar cantidad',
        }
class AforoAlmacenamientoVehicularForm(forms.ModelForm):
    class Meta:
        model = AforoAlmacenamientoVehicular
        fields = ['vehiculo','cantidad','porcion_almacenada','frec_operacion']
     
        widgets = {
            'vehiculo': forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
            'porcion_almacenada':forms.Select(attrs={'class':'form-control'}),
            'frec_operacion':forms.NumberInput(attrs={'class':'form-control'}),

            
        }

        labels={
            'vehiculo':'Seleccionar vehículo',
            'cantidad':'Ingresar cantidad',
            'porcion_almacenada':'Ingresar porción almacenada',
            'frec_operacion':'Ingresar Frecuencia de operación (Horas/año)',
        }
class ExtraccionAguaForm(forms.ModelForm):
    class Meta:
        model = ExtraccionAgua
        fields = ['pozo','velocidad']
     
        widgets = {
            'pozo': forms.TextInput(attrs={'class':'form-control'}),
            'velocidad':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'pozo':'Ingresar pozo',
            'velocidad':'Ingresar velocidad en L/s',
        }
class FrecuenciaActComForm(forms.ModelForm):
    class Meta:
        model = FrecuenciaActCom
        fields = ['actividad','cantidad']
     
        widgets = {
            'actividad': forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'actividad':'Seleccionar actividad',
            'cantidad':'Ingresar Jornadas/etapa',
        }
class AforoVisitantesForm(forms.ModelForm):
    class Meta:
        model = AforoVisitantes
        fields = ['actividad','maximo_etapa','promedio_diario','maximo_diario']
     
        widgets = {
            'actividad': forms.Select(attrs={'class':'form-control'}),
            'maximo_etapa':forms.NumberInput(attrs={'class':'form-control'}),
            'promedio_diario':forms.NumberInput(attrs={'class':'form-control'}),
            'maximo_diario':forms.NumberInput(attrs={'class':'form-control'}),

           
        }
        labels={
            'actividad':'Seleccionar actividad',
            'maximo_etapa':'Ingresar máximo de visitantes por etapa',
            'promedio_diario':'Ingresar promedio de visitantes por etapa',
            'maximo_diario':'Ingresar máximo de visitantes diarios',
        }
class OcupacionAlojaForm(forms.ModelForm):
    class Meta:
        model = OcupacionAloja
        fields = ['cobertura','oferta','huespedes_dia','huespedes_etapa']
     
        widgets = {
            'cobertura': forms.Select(attrs={'class':'form-control'}),
            'oferta':forms.TextInput(attrs={'class':'form-control'}),
            'huespedes_dia':forms.NumberInput(attrs={'class':'form-control'}),
            'huespedes_etapa':forms.NumberInput(attrs={'class':'form-control'}),

           
        }
        labels={
            'cobertura':'Seleccionar cobertura',
            'oferta':'Ingresar oferta de alojamiento (equivalencia en cuarto doble/2 personas)',
            'huespedes_dia':'Ingresar número de huéspedes diarios',
            'huespedes_etapa':'Ingresar número de huéspedes por etapa',
        }
class AforoTipoVehiMaxDiarioForm(forms.ModelForm):
    class Meta:
        model = AforoTipoVehiMaxDiario
        fields = ['vehiculo','cantidad']
     
        widgets = {
            'vehiculo': forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'vehiculo':'Seleccionar tipo de vehiculo',
            'cantidad':'Ingresar cantidad de vehículos diarios',

        }
class AforoTipoVehiForm(forms.ModelForm):
    class Meta:
        model = AforoTipoVehi
        fields = ['vehiculo','cantidad']
     
        widgets = {
            'vehiculo': forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'vehiculo':'Seleccionar tipo de vehiculo',
            'cantidad':'Ingresar horas/etapa',

        }
class PersonalTransportadoForm(forms.ModelForm):
    class Meta:
        model = PersonalTransportado
        fields = ['minimo','maximo']
     
        widgets = {
            'minimo': forms.NumberInput(attrs={'class':'form-control'}),
            'maximo':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'minimo':'Ingresar mínimo',
            'maximo':'Ingresar máximo',
        }
class ManejoSustanciasEspecialesForm(forms.ModelForm):
    class Meta:
        model = ManejoSustanciasEspeciales
        fields = ['instalacion','area','actividad_especial','manejo_sustancias']
     
        widgets = {
            'instalacion': forms.Select(attrs={'class':'form-control'}),
            'area': forms.Select(attrs={'class':'form-control'}),
            'actividad_especial': forms.Select(attrs={'class':'form-control'}),
            'manejo_sustancias':forms.TextInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'instalacion':'Seleccionar instalación especial',
            'area':'Seleccionar área de manejo',
            'actividad_especial':'Seleccionar tipo de actividades',
            'manejo_sustancias':'Ingresar manejo de sustancias',
        }

class CapacidadAlmSustanciasEspecialesForm(forms.ModelForm):
    class Meta:
        model = CapacidadAlmSustanciasEspeciales
        fields = ['instalacion','sustancia','capacidad_alm','recargas','recargas_totales']
     
        widgets = {
            'instalacion': forms.Select(attrs={'class':'form-control'}),
            'sustancia': forms.Select(attrs={'class':'form-control'}),
            'capacidad_alm': forms.NumberInput(attrs={'class':'form-control'}),
            'recargas':forms.NumberInput(attrs={'class':'form-control'}),
            'recargas_totales':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'instalacion':'Seleccionar instalación especial',
            'sustancia':'Seleccionar sustancia',
            'capacidad_alm':'Ingresar capacidad de almacenamiento',
            'recargas':'Ingresar número de recargas al año',
            'recargas_totales':'Ingresar total de recargas en la etapa',
        }
class CapacidadAlmResiduosEspecialesForm(forms.ModelForm):
    class Meta:
        model = CapacidadAlmResiduosEspeciales
        fields = ['instalacion','residuo','capacidad_veh','viajes_anual','viajes_totales']
     
        widgets = {
            'instalacion': forms.Select(attrs={'class':'form-control'}),
            'residuo': forms.Select(attrs={'class':'form-control'}),
            'capacidad_veh': forms.NumberInput(attrs={'class':'form-control'}),
            'viajes_anual':forms.NumberInput(attrs={'class':'form-control'}),
            'viajes_totales':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'instalacion':'Seleccionar instalación especial',
            'residuo':'Seleccionar residuo',
            'capacidad_veh':'Ingresar capacidad de almacenamiento',
            'viajes_anual':'Ingresar número de viajes al año',
            'viajes_totales':'Ingresar total de viajes en la etapa',
        }
class FrecuenciaIngresoSusEspecialesForm(forms.ModelForm):
    class Meta:
        model = FrecuenciaIngresoSusEspeciales
        fields = ['instalacion','sustancia','capacidad_veh','viajes_anual','viajes_totales']
     
        widgets = {
            'instalacion': forms.Select(attrs={'class':'form-control'}),
            'sustancia': forms.Select(attrs={'class':'form-control'}),
            'capacidad_veh': forms.NumberInput(attrs={'class':'form-control'}),
            'viajes_anual':forms.NumberInput(attrs={'class':'form-control'}),
            'viajes_totales':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'instalacion':'Seleccionar instalación especial',
            'sustancia':'Seleccionar sustancia',
            'capacidad_veh':'Ingresar capacidad de almacenamiento',
            'viajes_anual':'Ingresar número de viajes al año',
            'viajes_totales':'Ingresar total de viajes en la etapa',
        }

class FrecuenciaIngresoResEspecialesForm(forms.ModelForm):
    class Meta:
        model = FrecuenciaIngresoResEspeciales
        fields = ['instalacion','residuo','capacidad_veh','viajes_anual','viajes_totales']
     
        widgets = {
            'instalacion': forms.Select(attrs={'class':'form-control'}),
            'residuo': forms.Select(attrs={'class':'form-control'}),
            'capacidad_veh': forms.NumberInput(attrs={'class':'form-control'}),
            'viajes_anual':forms.NumberInput(attrs={'class':'form-control'}),
            'viajes_totales':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'instalacion':'Seleccionar instalación especial',
            'residuo':'Seleccionar residuo',
            'capacidad_veh':'Ingresar capacidad de almacenamiento',
            'viajes_anual':'Ingresar número de viajes al año',
            'viajes_totales':'Ingresar total de viajes en la etapa',
        }
class MaquinariaViajesEspForm(forms.ModelForm):
    class Meta:
        model = MaquinariaViajesEsp
        fields = ['instalacion','maquinaria','unidades','viajes','gasolina','diesel','aceites','anticongelante','liq_frenos','lubricantes']
     
        widgets = {
            'instalacion': forms.Select(attrs={'class':'form-control'}),
            'maquinaria': forms.Select(attrs={'class':'form-control'}),
            'unidades':forms.NumberInput(attrs={'class':'form-control'}),
            'viajes':forms.NumberInput(attrs={'class':'form-control'}),
            'gasolina':forms.NumberInput(attrs={'class':'form-control'}),
            'diesel':forms.NumberInput(attrs={'class':'form-control'}),
            'aceites':forms.NumberInput(attrs={'class':'form-control'}),
            'anticongelante':forms.NumberInput(attrs={'class':'form-control'}),
            'liq_frenos':forms.NumberInput(attrs={'class':'form-control'}),
            'lubricantes':forms.NumberInput(attrs={'class':'form-control'}),

           
        }
        labels={
            'instalacion':'Seleccionar instalación especial',
            'maquinaria':'Seleccionar maquinaria',
            'unidades':'Ingresar número de unidades',
            'viajes':'Ingresar número de viajes por unidad',
            'gasolina':'Ingresar cantidad de gasolina (L)',
            'diesel':'Ingresar cantidad de diesel (L)',
            'aceites':'Ingresar cantidad de aceites (L)',
            'anticongelante':'Ingresar cantidad de anticongelante (L)',
            'liq_frenos':'Ingresar cantidad de líquido de frenos (L)',
            'lubricantes':'Ingresar cantidad de lubricantes (L)',
        }
class TratamientoAguasResidualesForm(forms.ModelForm):
    class Meta:
        model = TratamientoAguasResiduales
        fields = ['ptar','cantidad']
     
        widgets = {
            'ptar': forms.Select(attrs={'class':'form-control'}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control'}),
           
        }
        labels={
            'ptar':'seleccionar PTAR',
            'cantidad':'Ingresar cantidad en L/s',
        }