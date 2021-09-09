from django.shortcuts import render
from.models import Question, Anwsers
# Create your views here.

def polls_list(request):
    poll = Question.objects.all()
    ANS = Anwsers.objects.all()
    return render(request,
                  'my_polls/question.html',
                  {'poll': poll,
                   'ANS':ANS
                   })