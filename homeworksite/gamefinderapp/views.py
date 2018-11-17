from django.shortcuts import render
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

def results(request, console_param, genre_param, age_class_param):
    game_found = Game.objects.filter(console = console_param, genre = genre_param, age_restriction = age_param)
    return HttpResponse("You're looking at game %s." % game_id)