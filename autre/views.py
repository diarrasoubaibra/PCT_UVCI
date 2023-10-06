from django.shortcuts import render

from autre.models import Competence, Metier

# Create your views here.
def metier(request):
    metiers = Metier.objects.all()
    return render(request, 'autre/metier.html',{'metiers': metiers})

def competence(request):
    competences = Competence.objects.all()
    return render(request, 'autre/competence.html',{'competences': competences})