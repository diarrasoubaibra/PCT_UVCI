from django.shortcuts import get_object_or_404, render
from datetime import date
from pharmacie.models import pharmacie

# Create your views here.
def pharmacie_views(request):
    pharmacies = pharmacie.objects.all()
    return render(request, 'pharmacie/pharmacie.html',{'pharmacies': pharmacies})

def pharmacie_details(request, id):
    pharmacie_details= get_object_or_404(pharmacie, pk=id)
    return render(request, 'pharmacie/pharmacie_details.html',{'pharmacie_details': pharmacie_details})


def pharmacie_de_garde_views(request):

    pharmacies = pharmacie.objects.all().filter(status=True)
    return render(request, 'pharmacie/pharmacie_de_garde.html',{'pharmacies': pharmacies})
