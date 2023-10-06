from datetime import datetime
from django.db import models

# Create your models here.
from django.db import models

class DemandeEmploi(models.Model):
    nom = models.CharField(max_length=100)
    service_offert = models.CharField(max_length=200)
    competences = models.TextField()
    contact_tel = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='static/images/demande_emplois/')
    message = models.TextField()
    status = models.BooleanField(default=False)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.service_offert}"


class OffreEmploi(models.Model):
    CONTRAT_CHOICES = (
        ('cdi', 'CDI'),
        ('cdd', 'CDD'),
        ('freelance', 'Freelance')
    )

    nom_entrep = models.CharField(max_length=100)
    titre = models.CharField(max_length=200)
    nombre_place = models.IntegerField()
    type_contrat = models.CharField(max_length=100, choices= CONTRAT_CHOICES)
    description_offre = models.CharField(max_length=500)
    competences_requises = models.TextField()
    contact = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='static/images/offre_emplois',blank=True, null=True )
    localisation = models.TextField()
    status = models.BooleanField(default=False)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.nom_entrep} - {self.titre}"

    def is_valid(self):
        now = datetime.now()
        return self.end_date > now
    