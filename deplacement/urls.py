from django.urls import path

from deplacement.views import amenagement

urlpatterns = [
    path('amenagement', amenagement, name="amenagement"),
]