from django import forms

class  LoginForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    mail = forms.EmailField(required=True)
    
class JuegosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    genero = forms.CharField(max_length=50, required=True)
    clasificacion = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)

class FigurasForm(forms.Form):
    nombre= forms.CharField(max_length=50, required=True)
    saga= forms.CharField(max_length=50, required=True)
    precio= forms.IntegerField(required=True)
    
class ComentarioForm(forms.Form):
    comentario=forms.CharField(max_length=280, required=True)