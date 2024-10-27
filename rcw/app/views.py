# app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import JobOffer
from .forms import JobForm, RegistrationForm, LoginForm

def index(request):
    """Page d'accueil"""
    return render(request, 'index.html')

def job_list(request):
    """Liste des offres d'emploi disponibles"""
    jobs = JobOffer.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

@login_required
def post_job(request):
    """Publier une offre d'emploi (réservé aux recruteurs)"""
    if request.user.role == 'RECRUTEUR':
        if request.method == 'POST':
            form = JobForm(request.POST)
            if form.is_valid():
                job = form.save(commit=False)
                job.recruteur = request.user.recruteur  # Associe l'offre au recruteur connecté
                job.save()
                return redirect('job_list')
        else:
            form = JobForm()
        return render(request, 'post_job.html', {'form': form})
    else:
        return redirect('job_list')  # Les candidats ne peuvent pas accéder à cette vue

@login_required
def profile(request):
    """Profil utilisateur"""
    return render(request, 'profile.html', {'user': request.user})

def register(request):
    """Inscription de nouveaux utilisateurs"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte l'utilisateur automatiquement après l'inscription
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    """Connexion utilisateur"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Nom d’utilisateur ou mot de passe incorrect')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    """Déconnexion utilisateur"""
    logout(request)
    return redirect('index')
