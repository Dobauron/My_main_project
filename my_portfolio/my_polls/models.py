from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=250)
    question = models.CharField(max_length=500)

    #Question model for poll

    def __str__(self):
        return self.title

class Anwsers(models.Model):
    anwser1 = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                )
    anwser2 = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                )
    anwser3 = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                )
    anwser4 = models.ForeignKey(Question,
                                on_delete=models.CASCADE,
                                )
