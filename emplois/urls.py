from django.urls import path
from emplois.views import affiche_demande, affiche_offre, demande_emplois, detail_demande

urlpatterns = [
    path('demande_emplois', demande_emplois, name="demande_emplois"),
    path('affiche_demande', affiche_demande, name="affiche_demande"),
    path('details_demande/<int:id>', detail_demande, name="details_demande"),
    path('affiche_offre', affiche_offre, name="affiche_offre"),
]