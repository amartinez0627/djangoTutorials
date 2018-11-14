from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Game

# Create your views here.
def index(request):
    game_list = Game.objects.order_by('id')[:10]
    template  = loader.get_template('gamefinderapp/index.html')
    context = {
        'game_list':game_list,
    }
    return HttpResponse(template.render(context,request))

def results(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)