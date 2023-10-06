from django.shortcuts import render

from medecine.models import Centre_santes, Epidemies, Maladies

# Create your views here.
def medecine_view(request):
    maladies = Maladies.objects.all()
    epidemies = Epidemies.objects.all()
    context = {
        'maladies' : maladies,
        'epidemies' : epidemies,
    }
    return render(request, 'medecine/medecine.html',context)

def centre_sante_view(request):
    centre_santes = Centre_santes.objects.all()
    return render(request, 'medecine/centre_sante.html',{'centre_santes':centre_santes} )

