# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offres/', views.job_list, name='job_list'),
    path('offres/poster/', views.post_job, name='post_job'),
    path('profil/', views.profile, name='profile'),
    path('inscription/', views.register, name='register'),
    path('connexion/', views.login_view, name='login'),
    path('deconnexion/', views.logout_view, name='logout'),
]
