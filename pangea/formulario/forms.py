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
        fields = ['title','completo']
        #fields = ['title','componente','fase','etapa','completo']
        
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control','readonly':'readonly',}),
            # 'componente': forms.Select(attrs={'class':'form-control','readonly':'readonly','disabled':'disabled'}),
            # 'fase': forms.Select(attrs={'class':'form-control','readonly':'readonly','disabled':'disabled'}),
            # 'etapa': forms.Select(attrs={'class':'form-control','readonly':'readonly','disabled':'disabled'}),
            'completo': forms.CheckboxInput(attrs={'class':'form-control ml-2'}),
            }

        labels = {
            'completo':'Marcar como completo y verificado / Desactivar para pendiente'
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