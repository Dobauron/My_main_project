from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.



class Item(models.Model):
    name = models.CharField(max_length=50)
    strengh = models.IntegerField()
    inteligence = models.IntegerField()
    dextrity = models.IntegerField()

    def __str__(self):
        return self.name



class Monster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    strengh = models.IntegerField()
    inteligence = models.IntegerField()
    dextrity = models.IntegerField()
    damage = models.IntegerField()
    health_point = models.IntegerField()

    def __str__(self):
        return self.name

class Land(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    enterance_cost = models.IntegerField()
    monster_set = models.ManyToManyField(Monster)

#     story_set
    def __str__(self):
        return self.name


class Player(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    inteligence = models.IntegerField(default=3)
    strengh = models.IntegerField(default=3)
    dextrity = models.IntegerField(default=3)
    localization = models.ForeignKey(Land, on_delete=models.CASCADE, default=id(1))
    damage = models.IntegerField(default=7)
    health_point = models.IntegerField(default=20)
    travel_sustain = models.IntegerField(default=10)
    doc = models.DateTimeField(default=datetime.now)


    class Meta:
        ordering = ('doc',)


    def __str__(self):
        return self.name
