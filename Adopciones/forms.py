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
    #Widgets
    def __init__(self, *args, **kwargs):
        print('paso constructor')
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs.update(placeholder='Ingrese sus nombres completos')
        self.fields['nombres'].widget.attrs.update(size='20')
        self.fields['nombres'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['edad'].widget.attrs.update(placeholder='Ingresa tu edad')
        self.fields['edad'].widget.attrs.update(size='20')
        self.fields['edad'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['genero'].widget.attrs.update(placeholder='Ingrese su gènero(Hembra/Macho)')
        self.fields['genero'].widget.attrs.update(size='25')
        self.fields['genero'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['animal'].widget.attrs.update(placeholder='Ingrese el tipo de mascota')
        self.fields['animal'].widget.attrs.update(size='15')
        self.fields['animal'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['descripcion'].widget.attrs.update(placeholder='Ingrese una o dos caracterìsticas de su mascota')
        self.fields['descripcion'].widget.attrs.update(size='25')
        self.fields['descripcion'].widget.attrs.update({'class': 'form-crontrol'})
    #ValidationError
    def clean_nombres(self, *args, **kwargs):
        print('paso: clean_nombre')
        name = self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('Debe colocar la primera letra en mayùscula')
    def clean_genero(self, *args, **kwargs):
        print('paso: clean_genero')
        genero = self.cleaned_data.get('genero')
        if genero.istitle():
            return genero
        else:
            raise forms.ValidationError('Debe colocar la primera letra en mayùscula')
    def clean_animal(self, *args, **kwargs):
        print('paso: clean_animal')
        animal = self.cleaned_data.get('animal')
        if animal.istitle():
            return animal
        else:
            raise forms.ValidationError('Debe colocar la primera letra en mayùscula')


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
    def __init__(self, *args, **kwargs):
        print('paso constructor')
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update(placeholder='Ingrese su nombre')
        self.fields['nombre'].widget.attrs.update(size='20')
        self.fields['nombre'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['apellido'].widget.attrs.update(placeholder='Ingrese su apellido')
        self.fields['apellido'].widget.attrs.update(size='20')
        self.fields['apellido'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['direccion'].widget.attrs.update(placeholder='Ingrese su direcciòn')
        self.fields['direccion'].widget.attrs.update(size='25')
        self.fields['direccion'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['correo'].widget.attrs.update(placeholder='Ingrese su correo electrònico')
        self.fields['correo'].widget.attrs.update(size='25')
        self.fields['correo'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['edad'].widget.attrs.update(placeholder='Ingresa tu edad(18+)')
        self.fields['edad'].widget.attrs.update(size='20')
        self.fields['edad'].widget.attrs.update({'class': 'form-crontrol'})
        self.fields['telefono'].widget.attrs.update(placeholder='Ingresa su numero telefònico')
        self.fields['telefono'].widget.attrs.update(size='20')
        self.fields['telefono'].widget.attrs.update({'class': 'form-crontrol'})

    #ValidationError
    def clean_nombre(self, *args, **kwargs):
        print('paso: clean_nombre')
        nombre = self.cleaned_data.get('nombre')
        if nombre.istitle():
            return nombre
        else:
            raise forms.ValidationError('Debe colocar la primera letra en mayùscula')
    def clean_apellido(self, *args, **kwargs):
        print('paso: clean_apellido')
        apellido = self.cleaned_data.get('apellido')
        if apellido.istitle():
            return apellido
        else:
            raise forms.ValidationError('Debe colocar la primera letra en mayùscula')
    def clean_direccion(self, *args, **kwargs):
        print('paso: clean_direccion')
        direccion = self.cleaned_data.get('direccion')
        if direccion.istitle():
            return direccion
        else:
            raise forms.ValidationError('Debe colocar la primera letra en mayùscula')
    def clean_correo(self, *args, **kwargs):#Falta
        print('paso: clean_correo')
        correo = self.cleaned_data.get('correo')
        if correo:
            return correo
        else:
            raise forms.ValidationError('Correo electrònico invàlido')
    def clean_edad(self, *args, **kwargs):
        print('paso: clean_edad')
        edad = self.cleaned_data.get('edad')
        if 18 <= edad:
            return edad
        else:
            raise forms.ValidationError('Usted debe ser mayor de edad para adoptar')
    def clean_telefono(self, *args, **kwargs):
        print('paso: clean_telefono')
        telefono = self.cleaned_data.get('telefono')
        if len(str(telefono)) == 9:
            return telefono
        else:
            raise forms.ValidationError('Este no es un número de telefono válido')

    
    

