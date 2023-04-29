from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        return password1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email or ('.com' not in email and '.co' not in email) or len(email) < 6:
            raise forms.ValidationError("Ingrese un email válido.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una cuenta asociada a este correo electrónico.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','avatar']
        help_texts = {k: '' for k in fields}


class MiFormularioCambioContraseña(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Modificar el campo new_password1 para eliminar la especificación de longitud
        self.fields['new_password1'].help_text = None

class EdicionPerfil(UserChangeForm):
    username = forms.CharField(label="Nombre de usuario", max_length=30, required=True)
    email = forms.EmailField(required=True, help_text="Ingrese un email válido.")
    first_name = forms.CharField(label = "Nombre", max_length=20)
    last_name = forms.CharField(label = "Apellido", max_length=20)
    avatar = forms.ImageField(required=False)
    password = None # Eliminar el campo de contraseña

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.username
        self.fields['email'].initial = self.instance.email

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if email != self.instance.email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con este email.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if username != self.instance.username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ya existe una cuenta con este nombre de usuario.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user



    