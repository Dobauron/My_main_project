from django.shortcuts import render, get_object_or_404
from . models import Player
from django.views.generic import DetailView
from . forms import PlayerForm
from django.contrib.auth.models import User

# Create your views here.
#
# class travel_view(DetailView):
#     queryset = Player.objects.all()

def travel_view(request):

    if request.method == 'POST':
        player_form = PlayerForm(data=request.POST)
        if player_form.is_valid():

            player= player_form.save(commit=False)


    else:
        player_form = PlayerForm()
    return render(request,
                  'creation_hero.html',
                  {'player_form' : player_form,})

