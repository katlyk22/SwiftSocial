from django import forms

class PersonaForm(forms.Form):
    nombre= forms.CharField(max_length=100)
    apellido= forms.CharField(max_length=100)
    Apodo= forms.CharField(max_length=20)
    fecha_nacimiento= forms.DateField()

class BuscarPersonasForm(forms.Form):
    criterio_nombre =forms.CharField(max_length=100)