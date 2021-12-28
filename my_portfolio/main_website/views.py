from django.shortcuts import render
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
app_name = "main_website"
def index(request):
    return render(request, 'index.html')

def Who_amI(request):
    return render(request, 'Who_amI.html')




#urls.py - my_blog
# from django.urls import path
# from .views import Post
#
# urlpatterns = [
#     path('blog/', Post)
# ]