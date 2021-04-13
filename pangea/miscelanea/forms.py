from django import forms 
from .models import *
from cap2.models import Modulo
class ModuloForm(forms.ModelForm):

    class Meta:
        model = Modulo
        fields = ['title','t_base','t_aprov_edificable','t_obras','t_areas_verdes','t_aprov_lineal']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', "placeholder":"Nombre del componente"}),
            't_base':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_aprov_edificable':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_obras':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_areas_verdes':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
            't_aprov_lineal':forms.CheckboxInput(attrs={'class':'form-check-input ml-2'}),
        }

        labels = {'title':''}

        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if 'title' in self.changed_data:
            if Modulo.objects.filter(title = title).exists():
                raise forms.ValidationError("Este componente ya esta registrado")
        return title


class MaquinaForm(forms.ModelForm):

    class Meta:
        model = Maquina
        fields = ['tipo','combustible','hp','kwh']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control','placeholder':"Nombre de la maquina"}),
            'combustible':forms.Select(attrs={'class': 'form-control'}),
            'hp':forms.TextInput(attrs={'class': 'form-control'}),
            'kwh':forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'tipo':'',
            'combustible':'Energía / Combustible',
            'hp':'hp sólo para gasolina, diésel, gas lp y gas natural',
            'kwh':'kW·h sólo para eléctricidad, solar, eólica',


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