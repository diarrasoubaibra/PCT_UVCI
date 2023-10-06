from django.urls import path
from autre.views import competence, metier

urlpatterns = [
    path('competence', competence, name="competence"),
    path('metier', metier, name="metier"),  
]