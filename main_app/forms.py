from django import forms
from .models import Tecnico

class TecnicoForm(forms.ModelForm):  #AutoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'servicio', 'telefono', 'email', 'direccion', 'image'] 