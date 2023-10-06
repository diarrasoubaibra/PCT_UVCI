from django.urls import path
from medecine.views import centre_sante_view, medecine_view


urlpatterns = [
    path('sante', medecine_view, name="medecine_view"),
    path('centre_sante',centre_sante_view, name="centre_sante_view")
]