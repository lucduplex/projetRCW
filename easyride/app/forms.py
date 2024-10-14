import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    cell = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255, required=True)
    face_id = forms.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'cell', 'address', 'face_id', 'password1', 'password2')
        
        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=15, required=True)
    cell = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'cell', 'address')