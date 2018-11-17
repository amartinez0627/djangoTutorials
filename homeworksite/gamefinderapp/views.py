from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.template import loader
from .models import Game

# Create your views here.
def index(request):
    game_list = Game.objects.all()
    template  = loader.get_template('gamefinderapp/index.html')
    context = {
        'game_list':game_list,
    }
    return HttpResponse(template.render(context,request))

def results(request, console_param, genre_param, age_param):
    console_values=['PC','PS4','XB1']
    genre_values=['act','adv','sp','sho','mus','fig','rac']
    template = loader.get_template('gamefinderapp/results.html')
    age = find_rest(age_param)
    game_found = get_object_or_404( Game,
        console = console_values[console_param],
        genre = genre_values[genre_param],
        age_restriction = age)
    context={
        'game_found':game_found,
        }
    
    return HttpResponse(template.render(context,request))

def find_rest(age_param):
    if age_param <=100:
        if age_param >= 18:
            return 'Ao'
        elif age_param >= 17:
            return 'M'
        elif age_param >= 13:
            return 'T'
        elif age_param >=10:
            return 'E'
        elif age_param >=3:
            return 'eC'
    return 0

