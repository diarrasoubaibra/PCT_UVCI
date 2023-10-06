from django.shortcuts import get_object_or_404, redirect, render
from datetime import date, datetime
from emplois.models import DemandeEmploi, OffreEmploi
from datetime import date
from django.db.models import Q
# Create your views here.
def demande_emplois(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        service_offert = request.POST.get('service_offert')
        competences = request.POST.get('competences')
        contact_tel = request.POST.get('contact_tel')
        photo = request.POST.get('photo')
        message = request.POST.get('message')
        date_pub = request.POST.get('date_pub')

        demande_emplois = DemandeEmploi.objects.create(nom=nom,
                                                       service_offert=service_offert,
                                                       competences=competences,
                                                       contact_tel=contact_tel,
                                                       photo=photo,
                                                       message=message, date_pub=date_pub)
        print(demande_emplois)

        print('validé')
        return redirect('index')
    else:
        return render(request, 'emplois/demande_emplois.html')
    
def affiche_demande(request):
    demande_emplois = DemandeEmploi.objects.all().filter(status=True)
    return render(request, 'emplois/affiche_demande.html',{'demande_emplois': demande_emplois})


def detail_demande(request, id):
    demande_emploi = get_object_or_404(DemandeEmploi, pk=id)
    return render(request, 'emplois/details_demande.html',{'demande_emploi': demande_emploi})

def affiche_offre(request):
    now = datetime.now()
    offre_emplois = OffreEmploi.objects.filter(date_fin__gt=now, status=True)

    return render(request, 'emplois/affiche_offre.html',{'offre_emplois': offre_emplois})

 