from django.shortcuts import render

from deplacement.models import Amenagement, Denagement

# Create your views here.
def amenagement(request):
    amenagements = Amenagement.objects.all()
    demenagements = Denagement.objects.all()
    context = {
        'amenagements' : amenagements,
        'demenagements' : demenagements,
    }
    return render(request, 'deplacement/deplacement.html',context)
