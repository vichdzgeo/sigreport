from django import forms 
from .models import ImagenLocalizacionC



class FormLocalizacionC(forms.ModelForm):

    class Meta:
        model = ImagenLocalizacionC
        fields = ['title','componente','etapa','image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'componente': forms.Select(attrs={'class':'form-control'}),
            #'fase': forms.Select(attrs={'class':'form-control'}),
            'etapa': forms.Select(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),           
        }