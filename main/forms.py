from django import forms

class Contacto(forms.Form):
	nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class': 'name', 'placeholder': 'Nombre'})) 
	correo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class': 'email', 'placeholder': 'Correo'}))
	numero = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class': 'phone', 'placeholder': 'Telefono'}))
	texto = forms.CharField( widget=forms.Textarea(attrs={ 'class': 'message', 'cols': '30', 'rows': '10', 'placeholder':'Mensaje', 'id': 'message'}))
	archivo = forms.FileField(widget=forms.FileInput(attrs={'class': 'file'}))


class Ingreso(forms.Form):
	cedula = forms.CharField(max_length=11, widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Cedula', 'id': 'email2'}))
		


class CheckForm(forms.Form):
	text = forms.CharField( widget=forms.Textarea())


class Peticion(forms.Form):
	seleccion = forms.ChoiceField(choices=[('UNO', 'Cesrtificado de pago'), ('DOS', 'certifiado de trabajo'), ('TRES', 'certificado de seguro')], widget=forms.Select(), label="Escoja el documeto que desea solicitar")