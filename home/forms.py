from django import forms
from .models import Contacto


class FormularioContacto(forms.ModelForm):

    class Meta:
        model = Contacto

        fields = [
            'nombre',
            'correo',
            'mensaje',
        ]
        labels = {
            'nombre':'Nombre',
            'correo':'Correo',
            'mensaje':'Mensaje',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'name':"name",'class':'form-control my-input','id': 'name', 'placeholder':'Name', }),
            'correo': forms.TextInput(attrs={'class':'form-control my-input','id':"email",'placeholder':"Correo"}),
            'mensaje': forms.Textarea(attrs={'class':'form-control my-input','min':'0', 'name':'phone', 'id':'phone','placeholder':'Mensaje','rows':'4'}),

        }


