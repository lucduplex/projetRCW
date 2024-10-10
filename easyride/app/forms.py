from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    face_image = forms.ImageField(required=True)  # Ajouter un champ pour l'image faciale

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'face_image')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    face_image = forms.ImageField(required=True)  # Ajouter un champ pour l'image faciale