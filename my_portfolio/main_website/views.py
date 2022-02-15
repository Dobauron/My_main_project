from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth import authenticate, login

from django.contrib.auth import views
from django.http import HttpResponse
from django import forms
# Create your views here.
app_name = "main_website"

class pcd(views.PasswordChangeView):
    template_name = 'password_change_done.html'
    app_name = "main_website"

class Who_amI(ListView):
    template_name = 'Who_amI.html'
    queryset = []



class index(ListView):
    template_name = "index.html"
    queryset = []

@login_required
def dashboard(request):
    return render(request,
                'registration/dashboard.html',
                {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
