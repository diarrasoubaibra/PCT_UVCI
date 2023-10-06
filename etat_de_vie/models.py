from django.db import models

# Create your models here.

class Naissance(models.Model):
    MODE_CHOICES = (
        ('H', 'hopital'),
        ('Q', 'quartier'),
    )
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    nom_nouvau_nee = models.CharField(max_length=255)
    date_naiss = models.DateField()
    nom_du_pere = models.CharField(max_length=255)
    nom_dela_mere = models.CharField(max_length=255)
    lieu_habitation = models.CharField(max_length=1000)
    mode_naisance = models.CharField(choices=MODE_CHOICES, max_length=20)
    sexe = models.CharField(choices=SEXE_CHOICES, max_length=20)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_nouvau_nee
    
class Deces(models.Model):
    MODE_CHOICES = (
        ('H', 'hopital'),
        ('Q', 'quartier'),
    )
    SEXE_CHOICES = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    nom_defun = models.CharField(max_length=255)
    function = models.CharField(max_length=255)
    date_naiss = models.DateField()
    date_deces = models.DateField()
    raison_deces = models.TextField()
    mode_deces = models.CharField(choices=MODE_CHOICES, max_length=20)
    lieu_habitation = models.CharField(max_length=1000)
    sexe = models.CharField(choices=SEXE_CHOICES, max_length=20)
    nom_parent_ref = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_defun


