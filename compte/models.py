from django.db import models
from django.contrib.auth.models import AbstractUser
from deplacement.models import Amenagement, Denagement

from autre.models import Competence, Metier
from pharmacie.models import pharmacie
from familles.models import Famille
from medecine.models import Centre_santes, Maladies
# Create your models here.

# class Acteur(AbstractUser):
#     SEXE_CHOICES = (
#         ('masculin', 'Masculin'),
#         ('féminin', 'Féminin')
#     )

#     date_naiss = models.DateField(null=True, blank=True)
#     lieu_naiss = models.CharField(max_length=500, null=True, blank=True)
#     sexe = models.CharField(max_length=255, choices=SEXE_CHOICES, null=True, blank=True)
#     telephone = models.CharField(max_length=50, null=True, blank=True)
#     image = models.FileField(null=True, blank=True)
#     famille = models.OneToOneField(Famille, related_name='famille', on_delete=models.SET_NULL,null=True, blank=True )
#     maladie = models.ManyToManyField(Maladies, related_name='maladie' , null=True,  blank=True)
#     metier = models.OneToOneField(Metier, related_name='metier', on_delete=models.SET_NULL,null=True,  blank=True)
#     competence = models.ManyToManyField(Competence, related_name='competence', null=True,  blank=True )
#     def __str__(self):
#         return self.username



# Create your models here.

class Acteur(AbstractUser):
    
    SEXE_CHOICES = (
        ('masculin', 'Masculin'),
        ('féminin', 'Féminin'),

    )
    telephone = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(choices=SEXE_CHOICES, max_length=255, blank=True, null=True)
    date_naiss = models.DateField(auto_now=True, blank=True, null=True)
    lieu_naiss = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='photos/user', null=True, blank=True)
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE,  blank=True, null=True)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE, blank=True, null=True)
    maladie = models.ManyToManyField(Maladies, related_name="maladies",  blank=True, null=True)
    competence = models.ManyToManyField( Competence, related_name="competence",   blank=True, null=True)
    pharmacie = models.ManyToManyField(pharmacie, related_name="maladies",  blank=True, null=True)
    centre_sante = models.ManyToManyField( Centre_santes, related_name="competence",   blank=True, null=True)
    amenager = models.ManyToManyField(Amenagement, related_name="amenager",  blank=True, null=True)
    demenager = models.ManyToManyField(Denagement, related_name="demenager",   blank=True, null=True)
    famille = models.OneToOneField(Famille, related_name='famille', on_delete=models.SET_NULL,null=True, blank=True )
    maladie = models.ManyToManyField(Maladies, related_name='maladie' , null=True,  blank=True)
    metier = models.OneToOneField(Metier, related_name='metier', on_delete=models.SET_NULL,null=True,  blank=True)
    competence = models.ManyToManyField(Competence, related_name='competence', null=True,  blank=True )
    def __str__(self):
         return self.username


    def _str_(self):
        return self.username