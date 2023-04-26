from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        return password1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email or ('.com' not in email and '.co' not in email) or len(email) < 6:
            raise forms.ValidationError("Ingrese un email válido.")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class MiFormularioCambioContraseña(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Modificar el campo new_password1 para eliminar la especificación de longitud
        self.fields['new_password1'].help_text = None

class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nombre", max_length=20)
    last_name = forms.CharField(label = "apellido", max_length=20)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']
    