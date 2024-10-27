# app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, JobOffer

class RegistrationForm(UserCreationForm):
    """Formulaire d'inscription utilisateur"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role', 'plan_abonnement']

class LoginForm(forms.Form):
    """Formulaire de connexion"""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class JobForm(forms.ModelForm):
    """Formulaire de publication d'offre d'emploi"""
    class Meta:
        model = JobOffer
        fields = ['titre', 'description', 'competences_requises', 'salaire', 'localisation']
