from django.contrib import admin

from emplois.models import DemandeEmploi, OffreEmploi

# Register your models here.
admin.site.register(DemandeEmploi)
admin.site.register(OffreEmploi)