from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(max_length=10, required=True)
    face_image = forms.ImageField(required=False)  # Facultatif si l'utilisateur ne veut pas uploader de photo

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'password1', 'password2', 'face_image']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    face_image = forms.ImageField(required=True)  # Ajouter un champ pour l'image faciale