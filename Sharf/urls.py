from django.contrib import admin
from django.urls import path
from sharing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('ajouter_fichier/', views.ajouter_fichier, name='ajouter_fichier'),
    path('profile/', views.profile, name='profile'),
]