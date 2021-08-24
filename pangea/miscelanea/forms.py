from django import forms 
from .models import *
from cap2.models import Modulo,Etapa,Fase



### -- GENERALES -- ### 

class EtapaForm(forms.ModelForm):

    class Meta:
        model = Etapa
        fields = '__all__'
        widgets = {
            'fase':forms.Select(attrs={'class': 'form-control'}),
            'title':forms.NumberInput(attrs={'class': 'form-control'}),
            'inicio':forms.NumberInput(attrs={'class': 'form-control'}),
            'fin':forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {'fase':'Seleccionar la fase',
                    'title':"Ingresar el número de la etapa",
                    'inicio':"Ingresar el año de inicio",
                    'fin':'Ingresar el año  de fin'}
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
class ModuloForm(forms.ModelForm):

    class Meta:
        model = Modulo
        fields = ['title','abreviatura','t_aprov_edificable','t_obras','t_semipermanentes','t_areas_verdes','t_aprov_lineal',
                    "t_via_senderos",'t_hospedaje','t_actividad','t_aguas','t_plantas',"etapas"]
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'abreviatura':forms.TextInput(attrs={'class': 'form-control'}),
            #'t_base':forms.CheckboxInput(attrs={'class':'form-check-input ml-2','disables':'disabled'}),
            't_aprov_edificable':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_obras':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_semipermanentes':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_areas_verdes':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_aprov_lineal':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_via_senderos':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_hospedaje':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_actividad':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_aguas':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_plantas':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            'etapas': forms.SelectMultiple(attrs={'class':'form-control','size':"10"}),
        }

        labels = {'title':"Nombre del componente (solo primer caracter en mayúscula) ",'abreviatura':"Abreviatura (todas en mayúsculas)",'etapas':'Seleccionar etapas'}
        
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if Modulo.objects.filter(title = title).exists():
                raise forms.ValidationError("Este componente ya esta registrado")
        return title
class ListaTipoVehiculoForm(forms.ModelForm):

    class Meta:
        model =ListaTipoVehiculo
        fields = ['tipo','descripcion']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {'tipo':"Nombre del tipo de vehículo",
                'descripcion':"Descripción"}
        
        
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTipoVehiculo.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo
class VehiculoPorTipoForm(forms.ModelForm):
    ## POR COMPLETAR EL DE FILTRADO####
    class Meta:
        model =VehiculoPorTipo
        fields = ['vehiculo','tipo','combustible']
        widgets = {
            'vehiculo':forms.TextInput(attrs={'class': 'form-control'}),
            'tipo':forms.Select(attrs={'class': 'form-control'}),
            'combustible':forms.Select(attrs={'class': 'form-control'}),
                    }

        labels = {'vehiculo':"Nombre del vehículo",
                'tipo':"Seleccionar el tipo",
                'combustible':"Seleccionar el tipo de combustible",}
        
        
    # def clean_tipo(self):
    #     vehiculo = self.cleaned_data.get("vehiculo")
    #     if 'vehiculo' in self.changed_data:
    #         if VehiculoPorTipo.objects.filter(vehiculo = vehiculo).exists():
    #             raise forms.ValidationError("Este vehículo ya esta registrado")
    #     return vehiculo
class ListInsEspForm(forms.ModelForm):

    class Meta:
        model =ListInsEsp
        fields = ['tipo','abreviatura']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'abreviatura':forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {'tipo':"Ingresar el nombre de la instalación especial",
                'abreviatura':"Ingresar la abreviatura (Máx 10 caracteres)",
                }
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
class InsumosListaForm(forms.ModelForm):

    class Meta:
        model = InsumosLista
        fields = ['title','unidad','fase']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'fase':forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'title':'Agregar insumo',
        'unidad':'Seleccionar unidad de medida',
        'fase':'Seleccionar la fase'}
    
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        fase = self.data.get("fase")
        if 'title' in self.changed_data:
            if InsumosLista.objects.filter(fase=fase).filter(title = title).exists():
                raise forms.ValidationError("Este insumo ya esta registrado para esta fase")
        return title
class SustanciasQuimicasPForm(forms.ModelForm):

    class Meta:
        model = SustanciasQuimicasP
        fields = ['title','unidad','fase']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'fase':forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'title':'Agregar sustancia química',
        'unidad':'Seleccionar unidad de medida',
        'fase':'Seleccionar la fase',}
    def clean_title(self):
        title = self.cleaned_data.get("title")
        fase = self.data.get("fase")
        if 'title' in self.changed_data:
            if SustanciasQuimicasP.objects.filter(fase=fase).filter(title = title).exists():
                raise forms.ValidationError("Esta sustancia ya esta registrada para esta fase")
        return title
class ListaTipoPersonalForm(forms.ModelForm):

    class Meta:
        model = ListaTipoPersonal
        fields = ['tipo','descripcion','fase']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'fase':forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'tipo':'Agregar tipo de personal',
        'descripcion':'Agregar descripción',
        'fase':'Seleccionar la fase'}
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        fase = self.data.get("fase")
        if 'tipo' in self.changed_data:
            if ListaTipoPersonal.objects.filter(fase=fase).filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo de personal ya fue registrado para esta fase")
        return tipo
class ListaTipoResiduosSolidosForm(forms.ModelForm):

    class Meta:
        model = ListaTipoResiduosSolidos
        fields =  '__all__'
        exclude =('created','updated')
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'tipo':'Agregar tipo de residuos Sólidos',
                'unidad':'Seleccionar unidad',
                }
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTipoResiduosSolidos.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo
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
                'toxico':'Tóxico',
                'biologico':'Biológico infeccioso',

                }
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTipoResiduos.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo
class ListaActividadesForm(forms.ModelForm):

    class Meta:
        model = ListaActividades
        fields = ['actividad','fase']
        widgets = {
            'actividad':forms.TextInput(attrs={'class': 'form-control'}),
            'fase':forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'actividad':'Agregar actividad',
        'fase':'Seleccionar la fase'}
    def clean_actividad(self):
        actividad = self.cleaned_data.get("actividad")
        fase = self.data.get("fase")
        if 'actividad' in self.changed_data:
            if ListaActividades.objects.filter(fase=fase).filter(actividad = actividad).exists():
                raise forms.ValidationError("Esta actividad ya fue registrado para esta fase")
        return actividad
class ResiduosPeligrososForm(forms.ModelForm):

    class Meta:
        model = ResiduosPeligrosos
        fields = ['residuo','unidad','ins_especial']
        widgets = {
            'residuo':forms.TextInput(attrs={'class': 'form-control'}),
            'unidad':forms.Select(attrs={'class': 'form-control'}),
            'ins_especial':forms.Select(attrs={'class': 'form-control'}),

        }
        labels ={'residuo':'Agregar residuo peligroso',
        'unidad':'Seleccionar la unidad',
        'ins_especial':'Seleccionar la instalación especial'}
    def clean_residuo(self):
        residuo = self.cleaned_data.get("residuo")
        ins_especial = self.data.get("ins_especial")
        if 'residuo' in self.changed_data:
            if ResiduosPeligrosos.objects.filter(ins_especial=ins_especial).filter(residuo = residuo).exists():
                raise forms.ValidationError("Esta residuo ya fue registrado para esta instalación especial")
        return residuo
class ListaPTARForm(forms.ModelForm):

    class Meta:
        model = ListaPTAR
        fields = ['planta',]
        widgets = {
            'planta':forms.TextInput(attrs={'class': 'form-control'}),


        }
        labels={'planta':'Agregar nombre de planta de tratamiento',
        }
    def clean_planta(self):
        planta = self.cleaned_data.get("planta")
        if 'planta' in self.changed_data:
            if ListaPTAR.objects.filter(planta = planta).exists():
                raise forms.ValidationError("Esta planta ya esta registrada")
        return planta

#### --- TERMINA GENERALES --- ###
#### --- INCIA CONSTRUCCIÓN --- ###
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
        fields = ['tipo','combustible','hp','kwh','fase']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control',}),
            'combustible':forms.Select(attrs={'class': 'form-control'}),
            'hp':forms.TextInput(attrs={'class': 'form-control'}),
            'kwh':forms.TextInput(attrs={'class': 'form-control'}),
            'fase':forms.Select(attrs={'class': 'form-control'})
        }

        labels = {
            'tipo':'Ingresar nombre de la  maquinaria',
            'combustible':'Seleccionar el tipo de Energía o Combustible',
            'hp':'Agregar hp (caballos de fuerza) para maquinaria operada con gasolina, diésel, gas LP o gas natural',
            'kwh':'Agregar kW·h (kilovatio hora) para maquinaria operada con eléctricidad, solar o eólica',
            'fase':'Seleccionar fase'


        }
        
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        fase = self.data.get("fase")
        if 'tipo' in self.changed_data:
            if Maquina.objects.filter(fase=fase).filter(tipo = tipo).exists():
                raise forms.ValidationError("Esta maquina ya esta registrada para esta fase")
        return tipo
class EdificacionProvisionalForm(forms.ModelForm):

    class Meta:
        model = EdificacionProvisional
        fields = ['title',]
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title':'Ingresar obra provisional'}
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if EdificacionProvisional.objects.filter(title = title).exists():
                raise forms.ValidationError("Esta obra provisional ya esta registrada")
        return title
class ActividadProvisionalForm(forms.ModelForm):
    class Meta:
        model = ActividadProvisional
        fields = ['title',]
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels = {'title':'Ingresar actividad provisional',

        }
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if ActividadProvisional.objects.filter(title = title).exists():
                raise forms.ValidationError("Esta actividad ya esta registrado")
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
class ProcConstructivoForm(forms.ModelForm):

    class Meta:
        model = ProcConstructivo
        fields = ['title','content']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control',})

        }
        labels ={'title':'Agregar proceso constructivo',
                 'content':'Descripción del proceso constructivo'
                }
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if ProcConstructivo.objects.filter(title = title).exists():
                raise forms.ValidationError("Este proceso ya esta registrado")
        return title
class SisConstructivoForm(forms.ModelForm):

    class Meta:
        model = SisConstructivo
        fields = ['title','content']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control',})

        }
        labels ={'title':'Agregar sistema constructivo',
                 'content':'Descripción del sistema constructivo'
                }
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if SisConstructivo.objects.filter(title = title).exists():
                raise forms.ValidationError("Este sistema ya esta registrado")
        return title
class SisFigurasForm(forms.ModelForm):

    class Meta:
        model = SisFiguras
        fields = ['image','pie']
        
        widgets = {
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
class ListaTiposAprovechamientoForm(forms.ModelForm):

    class Meta:
        model = ListaTiposAprovechamiento
        fields = ['title','subtipo']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control',}),
            'subtipo':forms.Select(attrs={'class': 'form-control',}),
        }

        labels = {'title':'Ingresar el tipo de aprovechamiento',
        }

        
    # def clean_tipo(self):
    #     tipo = self.cleaned_data.get("tipo")
    #     if 'tipo' in self.changed_data:
    #         if ListaTiposAprovechamiento.objects.filter(tipo = tipo).exists():
    #             raise forms.ValidationError("Este tipo ya esta registrado")
    #     return tipo
class MovimientoTierraForm(forms.ModelForm):
    class Meta:
        model = MovimientoTierra
        fields = ['tipo','unidad']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control',}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {'tipo':'Ingresar el tipo','unidad':"Seleccionar unidad"
       
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
    
    def clean_tipo(self):
        tipo = self.cleaned_data.get("tipo")
        if 'tipo' in self.changed_data:
            if ListaTiposConsEdif.objects.filter(tipo = tipo).exists():
                raise forms.ValidationError("Este tipo ya esta registrado")
        return tipo
#### -- TERMINA CONSTRUNCCIÓN -- ####

### -- INICIA OPERACIÓN --- ####

class ListaAct_scrcForm(forms.ModelForm):
    class Meta:
        model = ListaAct_scrc
        fields = ['actividad','descripcion']
        widgets = {
            'actividad':forms.TextInput(attrs={'class': 'form-control',}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {'actividad':'Ingresar la actividad','descripcion':"Ingresar descripción"
       
        }
    
    def clean_actividad(self):
        actividad = self.cleaned_data.get("actividad")
        if 'actividad' in self.changed_data:
            if ListaAct_scrc.objects.filter(actividad = actividad).exists():
                raise forms.ValidationError("Esta actividad ya esta registrado")
        return actividad
class ListActVisitantesForm(forms.ModelForm):

    class Meta:
        model = ListActVisitantes
        fields = ['actividad',]
        widgets = {
            'actividad':forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        labels ={'actividad':'Agregar actividad'}
    
    
    def clean_actividad(self):
        actividad = self.cleaned_data.get("actividad")
        fase = self.data.get("fase")
        if 'actividad' in self.changed_data:
            if ListActVisitantes.objects.filter(fase=fase).filter(actividad = actividad).exists():
                raise forms.ValidationError("Esta actividad ya esta registrada")
        return actividad
class ListaAreasManejoPeligrosasForm(forms.ModelForm):

    class Meta:
        model = ListaAreasManejoPeligrosas
        fields = ['n_area',]
        widgets = {
            'n_area':forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        labels ={'n_area':'Agregar área de manejo de sustancias peligrosas'}
    
    
    def clean_actividad(self):
        n_area = self.cleaned_data.get("n_area")
       
        if 'n_area' in self.changed_data:
            if ListaAreasManejoPeligrosas.objects.filter(n_area = n_area).exists():
                raise forms.ValidationError("Esta área ya esta registrada")
        return n_area
class ListaActInsEspForm(forms.ModelForm):

    class Meta:
        model = ListaActInsEsp
        fields = ['actividad']
        widgets = {
            'actividad':forms.TextInput(attrs={'class': 'form-control'}),
           
        }
        labels ={'actividad':'Agregar actividad'}
    
    
    def clean_actividad(self):
        actividad = self.cleaned_data.get("actividad")
      
        if 'actividad' in self.changed_data:
            if ListaActInsEsp.objects.filter(actividad = actividad).exists():
                raise forms.ValidationError("Esta actividad ya esta registrada")
        return actividad
