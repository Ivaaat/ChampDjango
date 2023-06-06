from django.contrib import admin
from .models import Table, Champ

#admin.site.register(Table)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['name_team', 'name_champ', 'tours', 'logo','status']
    search_fields = ['name_team', 'name_champ']
    ordering = ['tours', 'points']



@admin.register(Champ)
class ChampAdmin(admin.ModelAdmin):
    list_display = ['name_champ']
