from django.db import models

# Create your models here.
class Actualite(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    photo = models.FileField(upload_to='static/images/actualite')
    date_pub = models.DateField()
    update_pub = models.DateField(auto_now=True)

    def __str__(self):
        return self.titre