from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import DocumentPartage


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label = "Password",
        strip = False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2= forms.CharField(
        label= "Confirmez le mot de passe",
        widget= forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip = False,
    )
    
    # Pour personnliser les option du formulaire
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")
        


class DocumentForm(forms.ModelForm):
    class Meta:
        model = DocumentPartage
        fields = ['Fichier', 'NomDocument', 'description']