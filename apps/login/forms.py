from django import forms
from apps.login.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'email',
            'contra',
        ]
        labels = {
            'email' : 'Email',
            'contra' : 'Contrasena',
        }
        widgets = {
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'contra' : forms.TextInput(attrs={'class':'form-control'}),
        }
