from pymongo import MongoClient
from .models import Table
from django.contrib.auth.models import User
from datetime import datetime


def add_db():
    db = MongoClient()['champ']
    table_collect = db['table_2022/2023']
    calendar_collect = db['calendar_2022/2023']
    user = User.objects.get(username='admin')
    for team_stat in table_collect.find({}):
        team = Table.objects.get(name_team = team_stat['team'])
        team.name_champ = calendar_collect.find_one({'country':team_stat['country'], 'title':{'$regex':team_stat['team']}})['champ']
        team.logo = team_stat['logo']
        team.name_team = team_stat['team']
        #team.author = user,
        team.tours = int(team_stat['games'])
        team.points = int(team_stat['points'])
        team.games = int(team_stat['games'])
        team.loses = int(team_stat['lose'])
        team.wins = int(team_stat['win'])
        team.draw = int(team_stat['draw'])
        team.goals_scored = int(team_stat['balls'].split('-')[0])
        team.goals_missed = int(team_stat['balls'].split('-')[1])
        team.updated = datetime.now()
        team.status = Table.Status.PUBLISHED
        team.save()
        # Table.objects.create(name_champ = calendar_collect.find_one({'country':team_stat['country'], 
        #                                                              'title':{'$regex':team_stat['team']}}['champ']),
        

#add_db()

def add_champ_name():
    pass