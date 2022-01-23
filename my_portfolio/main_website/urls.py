from django.urls import path
from .views import index, Who_amI
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', index, name="index"),
    path('Who_amI', Who_amI, name="Who_amI"),
    path('loginview/',auth_views.LoginView.as_view(), name ='loginview'),
    path('logoutview/',auth_views.LogoutView.as_view(), name ='logoutview'),
]

