from django import forms 
from .models import Maquina, Unidad

class MaquinaForm(forms.ModelForm):

    class Meta:
        model = Maquina
        fields = ['tipo','combustible','hp','kwh']
        widgets = {
            'tipo':forms.TextInput(attrs={'class': 'form-control'}),
            'combustible':forms.Select(attrs={'class': 'form-control'}),
            'hp':forms.TextInput(attrs={'class': 'form-control'}),
            'kwh':forms.TextInput(attrs={'class': 'form-control'}),
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