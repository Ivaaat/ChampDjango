from django.db import models
from django.core.validators import MinValueValidator, \
MaxValueValidator
from django.contrib.auth.models import User
from django.urls import reverse

def valid(name, min = 0, max = 100):
    return models.IntegerField(validators=[MinValueValidator(min),
                                            MaxValueValidator(max)],
                                            help_text='{} должны быть в диапазоне ({} to {})'.format(name, min, max))

class Table(models.Model):
    objects = models.Manager()
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    name_champ = models.CharField(max_length=100) 
    name_team = models.CharField(max_length=100)
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='champ_table')
    tours = valid('Тур', min = 1, max = 50)
    points = valid('Очки')
    games = valid('Игры')
    loses = valid('Поражения')
    wins = valid('Победы')
    draw = valid('Ничья')
    logo = models.ImageField()
    goals_scored = valid('Забитые мячи', max = 200)
    goals_missed = valid('Пропущенные мячи', max = 200)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                            choices=Status.choices,
                            default=Status.DRAFT)

    class Meta:
        ordering = ['-points', '-goals_scored', 'goals_missed']
        indexes = [
                models.Index(fields=['-points', 'name_champ']),
                ]


    def __str__(self):
        return '{} Тур {}'.format(self.name_team, self.tours)
    
    def get_absolute_url(self):
            champ = Champ.objects.get(name_champ = self.name_champ)
            return reverse('table:table_detailed',
                            args=[champ.slug, self.id])
    

class Champ(models.Model):
    objects = models.Manager()
    name_champ = models.CharField(max_length=100, unique=True) 
    logo = models.ImageField()
    num_tours = valid('Тур', min = 1, max = 50)
    slug = models.CharField(max_length=20, default='rpl') 

    def get_absolute_url(self):
            return reverse('table:table_list',
                            args=[self.slug])

  






