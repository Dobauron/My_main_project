from django.urls import path
from .views import travel_view


app_name = "traveler_games"


urlpatterns = (
    path('champ_name/', travel_view, name='creation_hero'),
)