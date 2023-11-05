from django.shortcuts import render
from guide_sc.models import Stats
from django.http import HttpResponse

def person(request):
    info = Stats.objects.all(

    )
    return render(request, 'infopers.html', context={'info': info})
