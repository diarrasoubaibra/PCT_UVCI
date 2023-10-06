from django.shortcuts import get_object_or_404, render

from actualite.models import Actualite

# Create your views here

def actualite(request):
    actualites = Actualite.objects.all()
    return render(request, 'actualite/actualite.html',{'actualites': actualites})

def detail_actualite(request, id):
    actualite = get_object_or_404(Actualite, pk=id)
    return render(request, 'actualite/detail_actualite.html',{'actualite': actualite})
