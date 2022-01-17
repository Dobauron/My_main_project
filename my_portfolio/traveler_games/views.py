from django.shortcuts import render
from . models import Player

# Create your views here.
def travel_view(request):
    return render(request, 'travel.html',)