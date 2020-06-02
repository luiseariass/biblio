from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
array_choices = (
(1,"Distrito Capital"),
(2,"Amazonas"),
(3,"Anzoátegui"),
(4,"Apure"),
(5,"Aragua"),
(6,"Barinas"),
(7,"Bolívar"),
(8,"Carabobo"),
(9,"Cojedes"),
(10,"Delta Amacuro"),
(11,"Falcón"),
(12,"Guárico"),
(13,"Lara"),
(14,"Mérida"),
(15,"Miranda"),
(16,"Monagas"),
(17,"Nueva Esparta"),
(18,"Portuguesa"),
(19,"Sucre"),
(20,"Táchira"),
(21,"Trujillo"),
(22,"Vargas"),
(23,"Yaracuy"),
(24,"Zulia"))


class SignUpForm(UserCreationForm):
    primer_nombre = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    apellido = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    correo = forms.EmailField(max_length=254, help_text='Requerido. Email verificable.')
    estado = forms.ChoiceField(choices=array_choices)

    class Meta:
        model = User
        fields = ('username', 'primer_nombre', 'apellido', 'correo', 'password1', 'password2', )