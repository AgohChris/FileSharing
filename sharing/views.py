from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm, DocumentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import DocumentPartage, Utilisateur

# Create your views here.

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'connexion.html')


@login_required
def acceuil(request):
    return render(request, 'acceuil.html')


def ajouter_fichier(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            utilisateur = Utilisateur.objects.get(email=request.user.email)  # Récupère l'utilisateur connecté
            document.utilisateur = utilisateur
            document.save()
            messages.success(request, "Fichier ajouté avec succès.")
            return redirect('acceuil')
        else:
            messages.error(request, "Erreur lors de l'ajout du fichier.")
    else:
        form = DocumentForm()
    return render(request, 'acceuil.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')


