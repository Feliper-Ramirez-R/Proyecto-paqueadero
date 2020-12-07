from django import forms 
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainapp.models import Transporte


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label = "Usuario",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa un usuario'
            }
        )
    )

    email = forms.CharField(
        label = "Email",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa un email',
                'type': 'email'
            }
        ),
        validators=[
            validators.EmailValidator('usa el formato "ejemplo@ejemplo.com"', 'invalid_email')
        ]
    )

    first_name = forms.CharField(
        label = "Nombre",
        widget=forms.TextInput(
            attrs={
               'placeholder': 'Ingresa un nombre',
               'name':"Nombre"
            }
        ),
        validators=[
            validators.RegexValidator('^[A-Za-z]*$', 'Usa solo letras !!', 'invalid_Nombre')
        ]
    )

   


    last_name = forms.CharField(
        label = "Apellidos",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa unos apellidos'
            }
        ),
        validators=[
            validators.RegexValidator('^[A-Za-z]*$', 'Usa solo letras !!', 'invalid_user')
        ]
    )

    password1 = forms.CharField(
        label = "Contraseña",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa una contraseña',
                 'type': 'password'
                
            }
        )
    )

    password2 = forms.CharField(
        label = "Contraseña",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Confirma la contraseña',
                'type': 'password'
            }
        )
    )

   
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name', 'password1', 'password2' ]
        
      
        




    














   
    