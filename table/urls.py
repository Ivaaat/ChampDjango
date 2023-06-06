from django.urls import path
from . import views

app_name = 'table'

urlpatterns = [
# представления поста
#path('', views.champ_list, name='champ_list'),
path('', views.ChampListView.as_view(), name='champ_list'),
path('<str:slug>/', views.table_list, name='table_list'),
path('<str:slug>/<int:id>/', views.table_detailed, name='table_detailed'),
]