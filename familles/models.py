from django.db import models

# Create your models here.
class Famille(models.Model):
    nom_de_famille = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    chef_de_famille = models.CharField(max_length=100)
    nombre_de_membres = models.PositiveIntegerField(default=1)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_de_famille
