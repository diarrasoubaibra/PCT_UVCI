from django.contrib import admin

from etat_de_vie.models import Naissance, Deces

# Register your models here.
admin.site.register(Naissance)
admin.site.register(Deces)