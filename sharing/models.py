from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=30)
    

class DocumentsPartage(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    NomDocument = models.CharField(max_length=255)
    Fichier = models.FileField(upload_to='documents/')
    description = models.TextField(blank=True, null=True)
    date_partage = models.DateTimeField(auto_now=True)