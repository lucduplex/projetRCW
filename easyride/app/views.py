from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages
import face_recognition
from django.core.exceptions import ValidationError


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        face_image = request.FILES.get('face_id')

        if username and password:
            # Authentification classique avec username et password
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Connexion de l'utilisateur après validation FaceID
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        elif face_image:
            try:
                # Charger l'image FaceID de l'utilisateur depuis le système
                known_image = face_recognition.load_image_file(user.face_id.path)
                        
                # Charger l'image envoyée dans le formulaire pour la comparaison
                unknown_image = face_recognition.load_image_file(face_image)

                # Extraire les encodages des visages
                known_encoding = face_recognition.face_encodings(known_image)
                unknown_encoding = face_recognition.face_encodings(unknown_image)

                if not known_encoding or not unknown_encoding:
                    raise ValidationError("Aucun visage détecté dans l'image.")

                # Comparer les deux visages
                results = face_recognition.compare_faces([known_encoding[0]], unknown_encoding[0])

                if results[0]:
                    # Connexion de l'utilisateur après validation FaceID
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Échec de la reconnaissance faciale.")
            except Exception as e:
                messages.error(request, f"Erreur lors de la vérification de FaceID : {e}")
        else:
            messages.error(request, "Veuillez entrer Nom d'utilisateur et mot de passe, ou veuillez vous connecter avec reconnaissance faciale.")
            
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, "Formulaire d'inscription invalide. Veuillez vérifier vos informations.")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    request.session.flush()  # Vider la session lors de la déconnexion
    return redirect('login')  # Redirection vers la page de connexion après déconnexion


def about_view(request):
    return render(request, 'about.html')  # Assurez-vous que 'about.html' existe dans vos templates
