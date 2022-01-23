from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.
app_name = "main_website"

def Who_amI(request):
    return render(request, 'Who_amI.html')


def index(request):
    return render(request,
                  'index.html',
                  {'section' : 'index'}
                )



