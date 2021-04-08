from django import forms 
from .models import ImagenLocalizacionC
from cap2.models import Modulo,Fase,Etapa
def regresa_instancia_title(key,modelo):
    objetos = modelo.objects.all()

    for i in objetos:
        if i.title == key:
            return i

class FormLocalizacionC(forms.ModelForm):

    class Meta:
        model = ImagenLocalizacionC
        fields = ['title','componente','fase','etapa','image']
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'componente': forms.Select(attrs={'class':'form-control'}),
            'fase': forms.Select(attrs={'class':'form-control'}),
            'etapa': forms.Select(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),           
        }
