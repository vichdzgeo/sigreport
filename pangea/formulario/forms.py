from django import forms 
from .models import *
from cap2.models import Modulo,Fase,Etapa
from ckeditor.widgets import CKEditorWidget

def regresa_instancia_title(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.title == key:
            return i



class DescripcionProcesosConstructivosForm(forms.ModelForm):
    class Meta:
        model = DescripcionProcesosConstructivos
        fields = '__all__'
        exclude =('created','updated')
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'proceso_constructivo': forms.Select(attrs={'class':'form-control'}),
            'contenido': forms.TextInput(attrs={'class':'form-control'}),
        }


class SeleccionSistemasConstructivosForm(forms.ModelForm):
    class Meta:
        model = SeleccionSistemasConstructivos
        fields = '__all__'
        exclude =('created','updated')
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'sistemas': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

        labels ={
            'sistemas':'Seleccionar sistemas constructivos'
        }


class DatosGeneralForm(forms.ModelForm):
    class Meta:
        model = DatosGeneral
        fields =  '__all__'
        exclude =('created','updated')
        widgets = { 
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'sup_aprov_total': forms.NumberInput(attrs={'class':'form-control'}),
            'sup_edi': forms.NumberInput(attrs={'class':'form-control'}),
            'sup_const_no_edi': forms.NumberInput(attrs={'class':'form-control'}),
            'nivel_max': forms.NumberInput(attrs={'class':'form-control'}),
            'zonificacion': forms.TextInput(attrs={'class':'form-control'})
        }
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
        fields = ['componente','fase','etapa','image']
        
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control'}),
            'fase': forms.Select(attrs={'class':'form-control'}),
            'etapa': forms.Select(attrs={'class':'form-control'}),
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
        fields = ['componente','fase','etapa','actividades','horas']
        #fields = ['actividades','horas']
        
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'actividades': forms.Select(attrs={'class':'form-control'}),
            'horas': forms.NumberInput(attrs={'class':'form-control'}),           
        }

class DescripcionGeneralForm(forms.ModelForm):
    class Meta:
        model = DescripcionGeneral
        fields = ['componente','fase','etapa','duracion','content']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'duracion': forms.TextInput(attrs={'class':'form-control',}),        
            'content': forms.TextInput(attrs={'class':'form-control',}),        
        }

        labels={
            'content':'Agregar la descripción'
        }
        

class DescripcionGeneralFigurasForm(forms.ModelForm):

    class Meta:
        model = DescripcionGeneralFiguras
        fields = ['componente','fase','etapa','image','pie']
        
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'pie': forms.TextInput(attrs={'class':'form-control'}),         
        }

class SuperficieObrasCForm(forms.ModelForm):
    class Meta:
        model = SuperficieObrasC
        fields = ['componente','fase','etapa','edificaciones','superficie']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'edificaciones': forms.Select(attrs={'class':'form-control'}),
            'superfice': forms.NumberInput(attrs={'class':'form-control'}),                   
        }

        labels={
            'edificaciones':'Seleccionar obra o edificación provisional temporal',
            'superficie':'Agregar la superficie en m²'
        }

class ConsumoAguaCForm(forms.ModelForm):
    class Meta:
        model = ConsumoAguaC
        fields = ['componente','fase','etapa','tipo','unidad','cantidad']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            
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
        fields = ['componente','fase','etapa','tipo','unidad','cantidad']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            
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
        fields = ['componente','fase','etapa','flor']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'flor': forms.Select(attrs={'class':'form-control'}),
            
        }

        labels={
            'flor':'Seleccionar el tipo de especie',

        }

class PersonalRequeridoForm(forms.ModelForm):
    class Meta:
        model = PersonalRequerido
        fields = ['componente','fase','etapa','personal','n_prot','n_rest','n_apro']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'personal': forms.Select(attrs={'class':'form-control'}),
            'n_prot': forms.NumberInput(attrs={'class':'form-control'}),
            'n_rest': forms.NumberInput(attrs={'class':'form-control'}),
            'n_apro': forms.NumberInput(attrs={'class':'form-control'}),
            
            
        }

        labels={
            'personal':'Seleccionar el tipo de personal',

        }

class MaquinariaZonificacionForm(forms.ModelForm):
    class Meta:
        model = MaquinariaZonificacion
        fields = ['componente','fase','etapa','maquinaria','n_prot','n_rest','n_apro']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'maquinaria': forms.Select(attrs={'class':'form-control'}),
            'n_prot': forms.NumberInput(attrs={'class':'form-control'}),
            'n_rest': forms.NumberInput(attrs={'class':'form-control'}),
            'n_apro': forms.NumberInput(attrs={'class':'form-control'}),
            
        }

        labels={
            'maquinaria':'Seleccionar el tipo de maquinaria',

        }


class ObrasLinealesLongitudesForm(forms.ModelForm):
    class Meta:
        model = ObrasLinealesLongitudes
        fields = ['componente','fase','etapa','tipo','longitud']
     
        widgets = {
            'componente': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'fase': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'etapa': forms.Select(attrs={'class':'form-control','readonly':'True'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'longitud': forms.NumberInput(attrs={'class':'form-control'}),                   
        }

        labels={
            'tipo':'Seleccionar obra lineal',
            'longitud':'Agregar longitud en Km'
        }