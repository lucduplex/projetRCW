from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    face_image = forms.ImageField(required=True)
    mobile_number = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'mobile_number', 'email', 'password1', 'password2', 'face_image']

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            raise forms.ValidationError("Le numéro de mobile doit être composé de 10 chiffres.")
        return mobile_number


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    face_image = forms.ImageField(required=True)
