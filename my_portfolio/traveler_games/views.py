from django.shortcuts import render, get_object_or_404
from . models import Player
from django.views.generic import DetailView
from . forms import NameForm

# Create your views here.
#
# class travel_view(DetailView):
#     queryset = Player.objects.all()

def travel_view(request):
    player = Player.objects.filter(id=1)


    if request.method == 'POST':
        name_form = NameForm(data=request.POST)
        if name_form.is_valid():
            new_name = name_form.save(commit=False)

            new_name.save()
    else:
        name_form = NameForm()
    return render(request,
                  'creation_hero.html',
                  {'player' : player,
                   'name_form' : name_form,})

