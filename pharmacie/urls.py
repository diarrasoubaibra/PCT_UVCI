from django.urls import path
from pharmacie.views import pharmacie_details, pharmacie_views, pharmacie_de_garde_views

urlpatterns = [
    path('pharmacie', pharmacie_views, name="pharmacie_views"),
    path('pharmacie/pharmacie_details/<int:id>', pharmacie_details, name="pharmacie_details"),
    path('pharmacie_de_garde', pharmacie_de_garde_views, name="pharmacie_de_garde_views"),
]