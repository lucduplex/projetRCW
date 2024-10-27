# app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [('CANDIDAT', 'Candidat'), ('RECRUTEUR', 'Recruteur')]
    STATUS_CHOICES = [('ACTIF', 'Actif'), ('EXPIRE', 'Expiré')]
    PLAN_CHOICES = [('BASIC', 'Basic'), ('PRO', 'Pro'), ('ENTERPRISE', 'Enterprise')]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    statut = models.CharField(max_length=7, choices=STATUS_CHOICES, default='ACTIF')
    plan_abonnement = models.CharField(max_length=10, choices=PLAN_CHOICES)

    def __str__(self):
        return self.username

class Recruteur(User):
    entreprise = models.CharField(max_length=100)
    secteur_activite = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.entreprise} - {self.username}"

class Candidat(User):
    cv = models.FileField(upload_to='cvs/')
    competences = models.TextField(blank=True)  
    lettres_motivation = models.TextField(blank=True)  

    def __str__(self):
        return f"{self.username} - Candidat"

class JobOffer(models.Model):
    recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE, related_name='offres')
    titre = models.CharField(max_length=100)
    description = models.TextField()
    competences_requises = models.TextField()  
    salaire = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    localisation = models.CharField(max_length=100)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
