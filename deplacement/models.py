from django.db import models

# Create your models here.
class Amenagement(models.Model):

    SEXE_CHOICES = (
        ('masculin', 'Masculin'),
        ('féminin', 'Féminin')
    )

    MODE_HEBER_CHOICES = (
        ('nouvelle habitation', 'Nouvelle Habitation'),
        ('chez parent', 'Chez Un Parent')
    )

    nom = models.CharField(max_length=255, null=True, blank=True)
    sexe = models.CharField(max_length=255, choices=SEXE_CHOICES, null=True, blank=True)
    function = models.CharField(max_length=255, null=True, blank=True)
    date_naiss = models.DateField(null=True, blank=True)
    provenance = models.CharField(max_length=255, null=True, blank=True )
    mode_heber = models.CharField(max_length=255, choices=MODE_HEBER_CHOICES, null=True, blank=True)
    nom_parent_acc = models.CharField(max_length=255, null=True, blank=True )
    lieu_habitation_fami = models.CharField(max_length=255, null=True, blank=True )
    statut = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
    

class Denagement(models.Model):

    SEXE_CHOICES = (
        ('masculin', 'Masculin'),
        ('féminin', 'Féminin')
    )

    nom = models.CharField(max_length=255, null=True, blank=True)
    sexe = models.CharField(max_length=255, choices=SEXE_CHOICES, null=True, blank=True)
    function = models.CharField(max_length=255, null=True, blank=True)
    date_naiss = models.DateField(null=True, blank=True)
    nouvelle_dest = models.CharField(max_length=255, null=True, blank=True )
    lieu_habitation_fami = models.CharField(max_length=255, null=True, blank=True )
    statut = models.BooleanField(default=False)

    def __str__(self):
        return self.nom