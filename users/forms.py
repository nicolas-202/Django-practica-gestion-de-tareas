from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username' : 'Nombre de usuario',
            'email' : 'Correo electrónico',
            'password1' : 'Contraseña',
            'password2' : 'Confirmar contraseña',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': "👤 Tu nombre de usuario",
            'email': '📩 correo@ejemplo.com',
            'password1': '👁️ Tu contraseña',
            'password2': '👁️ Repite la contraseña',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-input'
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]