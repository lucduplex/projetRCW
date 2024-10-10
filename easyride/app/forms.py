from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    face_image = forms.ImageField(required=True)  # Ajouter un champ pour l'image faciale
    mobile_number = forms.CharField(max_length=10, required=True)  # Ajouter un champ pour le numéro de mobile
    email = forms.CharField(max_length=255, required=True)  # Ajouter un champ pour le courriel

    class Meta:
        model = User
        fields = ('username', 'mobile_number', 'email', 'password1', 'password2', 'face_image')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    face_image = forms.ImageField(required=True)  # Ajouter un champ pour l'image faciale