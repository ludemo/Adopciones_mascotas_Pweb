from django import forms
from .models import Mascotas,Usuario
class MascotasForm(forms.ModelForm):
    class Meta:
        model = Mascotas
        fields = [
            'nombres',
            'edad',
            'genero',
            'animal',
            'descripcion',
            'imagen',
        ]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'correo',
            'edad',
            'telefono',
        ]
        widgets = {
            'nombre':forms.TextInput(attrs={'placeholder':"Quijote",'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'placeholder':"de la mancha",'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'placeholder':"av.siempreViva",'class':'form-control'}),
            'correo': forms.TextInput(attrs={'placeholder':"demo@example.com"}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'placeholder':"924417100",'class':'form-control'}),
        }