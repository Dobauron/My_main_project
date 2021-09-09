from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Who_amI(request):
    return render(request, 'who_amI.html')


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#urls.py - my_blog
# from django.urls import path
# from .views import Post
#
# urlpatterns = [
#     path('blog/', Post)
# ]