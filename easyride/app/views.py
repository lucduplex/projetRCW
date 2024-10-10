from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from .models import UserProfile
from .forms import LoginForm
from .models import UserProfile

def home_view(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    request.session.flush()  # Vider la session lors de la déconnexion
    return redirect('login')  # Redirection vers la page de connexion après déconnexion

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            profile = UserProfile.objects.create(user=user, mobile_number=mobile_number, email=email)
            profile.save_face_encoding(form.cleaned_data['face_image'])
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            face_image = form.cleaned_data['face_image']
            user = authenticate(request, username=username, password=password)
            if user:
                profile = UserProfile.objects.get(user=user)
                if profile.verify_face(face_image):
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error(None, "Reconnaissance faciale échouée")
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def about_view(request):
    return render(request, 'about.html')