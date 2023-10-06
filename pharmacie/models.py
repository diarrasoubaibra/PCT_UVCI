from django.db import models
from django.db import models

# Create your models here.
class pharmacie(models.Model):
    nom_phar = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    photo = models.FileField(upload_to='static/images/pharmacie')
    periode_de_garde = models.CharField(max_length=255, null=True, blank=True )
    localisation = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom_phar