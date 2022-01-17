from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=250)
    question = models.CharField(max_length=500)
    #Question model for poll

    def __str__(self):
        return self.question

class Anwsers(models.Model):

    answer = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                related_name= 'polls_answ')

    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Odpowiedz'
