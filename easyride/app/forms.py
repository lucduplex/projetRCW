import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.validators import RegexValidator

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    cell = forms.CharField(max_length=15, validators=[RegexValidator(regex=r'^(\D*514|\D*438)\D*\d{3}\D*\d{4}$', message="Le numéro de téléphone doit commencer par 514 ou 438 et doit comporter 15 chiffres.")], required=True)
    address = forms.CharField(max_length=255, required=True)
    face_id = forms.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'cell', 'address', 'face_id', 'password1', 'password2')
        
        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=15, required=True)
    cell = forms.CharField(max_length=15, validators=[RegexValidator(regex=r'^(\D*514|\D*438)\D*\d{3}\D*\d{4}$', message="Le numéro de téléphone doit commencer par 514 ou 438 et doit comporter 15 chiffres.")], required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'cell', 'address')
        
        
class ConfirmationOfPasswordForm(forms.Form):
    password = forms.CharField(required=True)