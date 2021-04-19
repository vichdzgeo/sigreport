from django import forms 
from .models import *
from cap2.models import Modulo





class ModuloForm(forms.ModelForm):

    class Meta:
        model = Modulo
        fields = ['title','abreviatura','t_aprov_edificable','t_obras','t_areas_verdes','t_aprov_lineal']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', "placeholder":"Nombre del componente"}),
            'abreviatura':forms.TextInput(attrs={'class': 'form-control', "placeholder":"Abreviatura"}),
            #'t_base':forms.CheckboxInput(attrs={'class':'form-check-input ml-2','disables':'disabled'}),
            't_aprov_edificable':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_obras':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_areas_verdes':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_aprov_lineal':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
        }

        labels = {'title':'','abreviatura':''}

        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if Modulo.objects.filter(title = title).exists():
                raise forms.ValidationError("Este componente ya esta registrado")
        return title

class ObrasLinealesForm(forms.ModelForm):

    class Meta:
        model = ObrasLineales
        fields = ['tipo',]
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),


        }
        labels={'tipo':'Agregar nombre de obra líneal',
        }
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ObrasLineales.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo

class MaquinaForm(forms.ModelForm):

    class Meta:
        model = Maquina
        fields = ['tipo','combustible','hp','kwh']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control',}),
            'combustible':forms.Select(attrs={'class': 'form-control'}),
            'hp':forms.TextInput(attrs={'class': 'form-control'}),
            'kwh':forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'tipo':'Ingresar nombre de la  maquinaria',
            'combustible':'Seleccionar el tipo de Energía o Combustible',
            'hp':'Agregar hp (caballos de fuerza) para maquinaria operada con gasolina, diésel, gas LP o gas natural',
            'kwh':'Agregar kW·h (kilovatio hora) para maquinaria operada con eléctricidad, solar o eólica',


        }
        
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if Maquina.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Esta maquina ya esta registrada")
        return tipo
class UnidadForm(forms.ModelForm):

    class Meta:
        model = Unidad
        fields = ['title','description']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),

        }
        labels={'title':'Agregar abreviatura de unidad de medida con base en el estándar del Sistema Internacional de Unidades',
                'description':'Agregar descripción'}

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if Unidad.objects.filter(title = title).exists():
                raise forms.ValidationError("Esta unidad ya esta registrada")
        return title
class EdificacionProvisionalForm(forms.ModelForm):

    class Meta:
        model = EdificacionProvisional
        fields = ['title','description']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),

        }
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if EdificacionProvisional.objects.filter(title = title).exists():
                raise forms.ValidationError("Esta edificación ya esta registrada")
        return title
class ActividadProvisionalForm(forms.ModelForm):

    class Meta:
        model = ActividadProvisional
        fields = ['title',]
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),

        }
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if ActividadProvisional.objects.filter(title = title).exists():
                raise forms.ValidationError("Esta actividad ya esta registrada")
        return title
class InsumosListaForm(forms.ModelForm):

    class Meta:
        model = InsumosLista
        fields = ['title','unidad']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'title':'Agregar sustancia química',
        'unidad':'Seleccionar unidad de medida',}
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if InsumosLista.objects.filter(title = title).exists():
                raise forms.ValidationError("Esten insumo ya esta registrado")
        return title
class SustanciasQuimicasPForm(forms.ModelForm):

    class Meta:
        model = SustanciasQuimicasP
        fields = ['title','unidad']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'title':'Agregar sustancia química',
        'unidad':'Seleccionar unidad de medida',}
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if SustanciasQuimicasP.objects.filter(title = title).exists():
                raise forms.ValidationError("Esta sustancia ya esta registrada")
        return title
class ListadoFloristicoForm(forms.ModelForm):

    class Meta:
        model = ListadoFloristico
        fields = ['familia','especie','nombre','forma','rescate']
        widgets = {
            'familia':forms.TextInput(attrs={'class': 'form-control'}),
            'especie':forms.TextInput(attrs={'class': 'form-control'}),
            'nombre':forms.TextInput(attrs={'class': 'form-control'}),
            'forma':forms.TextInput(attrs={'class': 'form-control'}),
            'rescate':forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'familia': 'Familia',
            'especie':'Especie',
            'nombre': 'Nombre común',
            'forma': 'Forma biológica',
            'rescate':'Criterios para rescate',

        }
        
    def clean_especie(self):
        especie = self.cleaned_data.get("especie")
        if 'especie' in self.changed_data:
            if ListadoFloristico.objects.filter(especie = especie).exists():
                raise forms.ValidationError("Esta especie ya fue registrada")
        return especie
class ListaTipoPersonalForm(forms.ModelForm):

    class Meta:
        model = ListaTipoPersonal
        fields = ['tipo','descripcion']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels ={'tipo':'Agregar tipo de personal',
        'descripcion':'Agregar descripción'}
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTipoPersonal.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo de personal ya fue registrado")
        return tipo
class ListaSisConstructivoForm(forms.ModelForm):

    class Meta:
        model = ListaSisConstructivo
        fields = ['sistema',]
        widgets = {
            'sistema':forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels ={'sistema':'Agregar sistema constructivo',

                }
        
    def clean_sistema(self):
        sistema = self.cleaned_data.get("sistema")
        if 'sistema' in self.changed_data:
            if ListaSisConstructivo.objects.filter(sistema = sistema).exists():
                raise forms.ValidationError("Este sistema ya esta registrado")
        return sistema

class DescripcionSisConstructivoForm(forms.ModelForm):

    class Meta:
        model = DescripcionSisConstructivo
        fields = ['sistema','content']
        widgets = {
            'sistema':forms.Select(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control',}),        

        }
        labels ={'sistema':'Agregar sistema constructivo',
                 'content':'Descripción del sistema constructivo',
                }
        
    def clean_sistema(self):
        sistema = self.cleaned_data.get("sistema")
        if 'sistema' in self.changed_data:
            if Descripcion.objects.filter(sistema = sistema).exists():
                raise forms.ValidationError("Este sistema ya esta registrado")
        return sistema

class ListaSisConstructivoFigurasForm(forms.ModelForm):

    class Meta:
        model = ListaSisConstructivoFiguras
        fields = ['sistema','image','pie']
        
        widgets = {
            'sistema': forms.Select(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'pie': forms.TextInput(attrs={'class':'form-control'}),         
        }

class ListaProcesoConstructivoForm(forms.ModelForm):

    class Meta:
        model = ListaProcesoConstructivo
        fields = ['proceso',]
        widgets = {
            'proceso':forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels ={'proceso':'Agregar proceso constructivo',
                }
    def clean_proceso(self):
        proceso = self.cleaned_data.get("proceso")
        if 'proceso' in self.changed_data:
            if ListaProcesoConstructivo.objects.filter(proceso = proceso).exists():
                raise forms.ValidationError("Este proceso ya esta registrado")
        return proceso
class ListaTipoResiduosForm(forms.ModelForm):

    class Meta:
        model = ListaTipoResiduos
        fields =  '__all__'
        exclude =('created','updated')
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'corrosivo': forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            'reactivo': forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            'explosivo': forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            'toxico': forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            'inflamable': forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            'biologico': forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            'edo_fisico': forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'tipo':'Agregar tipo de residuos',

                }
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTipoResiduos.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo
class TipoAguaForm(forms.ModelForm):

    class Meta:
        model = TipoAgua
        fields = ['tipo',]
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels ={'tipo':'Agregar tipo de agua',
                }
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if TipoAgua.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo
class TipoAguaResidualForm(forms.ModelForm):

    class Meta:
        model = TipoAguaResidual
        fields = ['tipo',]
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels ={'tipo':'Agregar tipo de agua residual',
                }
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if TipoAguaResidual.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo

class ListaTiposAprovechamientoForm(forms.ModelForm):

    class Meta:
        model = ListaTiposAprovechamiento
        fields = ['tipo']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control',}),
        }

        labels = {'tipo':'Ingresar el tipo de aprovechamiento',
        }

        
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTiposAprovechamiento.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo

class ListaTiposCoberturaForm(forms.ModelForm):
    class Meta:
        model = ListaTiposCobertura
        fields = ['tipo','abreviatura']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control',}),
            'abreviatura':forms.TextInput(attrs={'class': 'form-control text-uppercase',}),
        }
        labels = {'tipo':'Ingresar el nombre del tipo de cobertura',
        'abreviatura':'Ingresar la abreviatura (Máx 10 caracteres)',
        }
    
    def clean_title(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTiposCobertura.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo


class ListaZonificacionForm(forms.ModelForm):
    class Meta:
        model = ListaZonificacion
        fields = ['zona','abreviatura']
        widgets = {
            'zona':forms.TextInput(attrs={'class': 'form-control',}),
            'abreviatura':forms.TextInput(attrs={'class': 'form-control text-uppercase',}),
        }
        labels = {'zona':'Ingresar el nombre de la zona',
        'abreviatura':'Ingresar la abreviatura (Máx 10 caracteres)',
        }
    
    def clean_title(self):
        zona = self.cleaned_data.get("zona")
        if 'zona' in self.changed_data:
            if ListaZonificacion.objects.filter(zona = zona).exists():
                raise forms.ValidationError("Este zona ya esta registrado")
        return zona

class MovimientoTierraForm(forms.ModelForm):
    class Meta:
        model = MovimientoTierra
        fields = ['tipo']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control',}),
           
        }
        labels = {'tipo':'Ingresar el nombre de la zona',
       
        }
    
    def clean_title(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if MovimientoTierra.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo

class ListaTiposConsEdifForm(forms.ModelForm):
    class Meta:
        model = ListaTiposConsEdif
        fields = ['tipo',]
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels = {'tipo':'Ingresar el tipo de construcción o edificación',

        }
    
    def clean_title(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTiposConsEdif.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo
