from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=250)
    question = models.CharField(max_length=500)

    #Question model for poll

    def __str__(self):
        return self.question

class Anwsers(models.Model):

    first_anws = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                related_name= 'polls_anws1')
    second_anws = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                related_name= 'polls_anws2')
    third_anws = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                related_name= 'polls_anws3')
    fourth_anws = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                related_name= 'polls_anws4')
    def __str__(self):
        return 'Odpowiedz'
