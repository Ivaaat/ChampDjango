from rest_framework import serializers
from .models import Table
 
 
class ChampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('name_champ', 
                  'name_team',
                  'author',
                  'tours',
                  'points',
                  'games',
                  'loses',
                  'wins',
                  'draw',
                  'logo',
                  'goals_scored',
                  'goals_missed',
                  )