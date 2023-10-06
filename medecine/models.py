from django.db import models
# Create your models here.
class Epidemies(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    symptoms = models.CharField(max_length=500, null=True, blank=True)
    traitement = models.CharField(max_length=255, null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    nombre_cas = models.CharField(max_length=255, null=True, blank=True)
    nombre_mort = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nom


class Maladies(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    symptoms = models.CharField(max_length=500, null=True, blank=True)
    traitement = models.CharField(max_length=255, null=True, blank=True)
    epidemie = models.OneToOneField(Epidemies, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nom
    

    
class Centre_santes(models.Model):
    nom = models.CharField(max_length=255, null=True, blank=True)
    service = models.CharField(max_length=100)
    photo = models.FileField(upload_to='static/images/centre_sante')
    contact = models.CharField(max_length=50, null=True, blank=True)
    localisation = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
