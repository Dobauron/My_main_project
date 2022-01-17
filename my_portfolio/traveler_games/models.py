from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Item(models.Model):
    name = models.CharField(max_length=50)
    strengh = models.IntegerField()
    inteligence = models.IntegerField()
    dextrity = models.IntegerField()


class Monster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    strengh = models.IntegerField()
    inteligence = models.IntegerField()
    dextrity = models.IntegerField()
    damage = models.IntegerField()
    health_point = models.IntegerField()


class Land(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    enterance_cost = models.IntegerField()
    monster_set = models.ManyToManyField(Monster)
#     story_set


class Player(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    inteligence = models.IntegerField()
    strengh = models.IntegerField()
    dextrity = models.IntegerField()
    localization = models.ForeignKey(Land, on_delete=models.CASCADE)
    damage = models.IntegerField()
    health_point = models.IntegerField()
    travel_sustain = models.IntegerField()