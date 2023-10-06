from actualite.views import actualite, detail_actualite
from django.urls import path

urlpatterns = [
    path('actualite', actualite, name="actualite"),
    path('detail_actualite/<int:id>', detail_actualite, name="detail_actualite"),
]