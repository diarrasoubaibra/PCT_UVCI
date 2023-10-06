from django.db import models

# Create your models here.
class Metier(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    secteur = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.nom
    
class Competence(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.nom
