from django.shortcuts import render, get_object_or_404
from .models import Table, Champ
from django.views.generic import ListView
from .service import add_db
from rest_framework import generics
from .serializers import ChampSerializer

#add_db()

class ChampAPIView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = ChampSerializer

class ChampListView(ListView):
    queryset = Champ.objects.all()
    context_object_name = 'champs'
    template_name = 'champ.html'

def champ_list(request):
    return render(request, ChampListView.template_name, 
                            {ChampListView.context_object_name:
                             ChampListView.queryset})


def table_list(request, slug):
    champs = Champ.objects.get(slug=slug)
    teams = Table.objects.filter(name_champ=champs.name_champ)
    return render(request, 'table.html', {'teams':teams, 
                                          'champs':champs, 
                                          })


def table_detailed(request, slug, id):
    team_stat = get_object_or_404(Table, id=id)
    #team_stat = Table.objects.get(name_team=team)
    return render(request, 'team.html', {'team':team_stat})











