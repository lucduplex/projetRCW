import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth import authenticate
import face_recognition

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    cell = forms.CharField(max_length=15)
    face_id = forms.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'cell', 'face_id', 'password1', 'password2')