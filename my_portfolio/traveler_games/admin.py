from django.contrib import admin
from .models import Player,Monster,Land,Item
# Register your models here.

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('name','type', 'enterance_cost')
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('users', 'name','inteligence', 'strengh', 'dextrity', 'damage','health_point', 'travel_sustain')
@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ('name','type',  'inteligence', 'strengh', 'dextrity','damage','health_point',)
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'inteligence', 'strengh', 'dextrity')
