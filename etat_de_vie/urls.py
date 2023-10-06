from etat_de_vie.views import affiche_deces, soumettre_deces, soumettre_naissance, affiche
from django.urls import path

urlpatterns = [
    path('soumettre_naissance', soumettre_naissance, name="soumettre_naissance"),
    path('affiche_naissance', affiche, name="affiche_naissance"),
    path('soumettre_deces', soumettre_deces, name="soumettre_deces"),
    path('affiche_deces', affiche_deces, name="affiche_deces"),
]