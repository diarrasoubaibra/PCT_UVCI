from django.contrib import admin

# Register your models here.
from django.contrib import admin
from medecine.models import Centre_santes, Epidemies, Maladies

# Register your models here.

admin.site.register(Maladies)
admin.site.register(Epidemies)
admin.site.register(Centre_santes)