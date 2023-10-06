from django.shortcuts import redirect, render
from datetime import date
from etat_de_vie.models import Naissance, Deces

def affiche(request):
    today = date.today()
    naissances = Naissance.objects.all().filter(date_naiss=today).filter(status=True)
    return render(request, 'etat_de_vie/affiche_naissance.html',{'naissances': naissances})

def affiche_deces(request):
    today = date.today()
    deces = Deces.objects.all().filter(date_deces=today).filter(status=True)
    return render(request, 'etat_de_vie/affiche_deces.html',{'deces': deces})



def soumettre_naissance(request):
    if request.method == "POST":
        nom_nouvau_nee = request.POST.get('nom_nouvau_nee')
        date_naiss = request.POST.get('date_naiss')
        nom_du_pere = request.POST.get('nom_du_pere')
        nom_dela_mere = request.POST.get('nom_dela_mere')
        lieu_habitation = request.POST.get('lieu_habitation')
        mode_naisance = request.POST.get('mode_naisance')
        sexe = request.POST.get('sexe')

        naissance = Naissance.objects.create(nom_nouvau_nee=nom_nouvau_nee, date_naiss=date_naiss, nom_du_pere=nom_du_pere, nom_dela_mere=nom_dela_mere, lieu_habitation=lieu_habitation, mode_naisance=mode_naisance, sexe=sexe)
        print(naissance)

        print('validééééééééééééééééééééééééééééé')
        return redirect('index')
    else:
        return render(request, 'etat_de_vie/soumettre_naissance.html')
    

def soumettre_deces(request):
    if request.method == "POST":
        nom_defun = request.POST.get('nom_defun')
        function = request.POST.get('function')
        date_naiss = request.POST.get('date_naiss')
        date_deces = request.POST.get('date_deces')
        raison_deces = request.POST.get('date_deces')
        mode_deces = request.POST.get('mode_deces')
        lieu_habitation = request.POST.get('lieu_habitation')
        sexe = request.POST.get('sexe'),
        nom_parent_ref = request.POST.get('nom_parent_ref')

        deces = Deces.objects.create(nom_defun=nom_defun,
                                    function=function,
                                    date_naiss=date_naiss,
                                    date_deces=date_deces,
                                    raison_deces=raison_deces,
                                    mode_deces=mode_deces,
                                    lieu_habitation=lieu_habitation,
                                    sexe=sexe,
                                    nom_parent_ref=nom_parent_ref
                                    )
        print(deces)

        print('validééééééééééééééééééééééééééééé')
        return redirect('index')
    else:
        return render(request, 'etat_de_vie/soumettre_deces.html')