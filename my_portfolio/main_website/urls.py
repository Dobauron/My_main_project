from django.urls import path
from .views import index, Who_amI
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', index, name="index"),
    path('Who_amI', Who_amI, name="Who_amI"),
    path('loginview/',auth_views.LoginView.as_view(), name ='loginview'),
    path('logoutview/',auth_views.LogoutView.as_view(), name ='logoutview'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name= 'password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.register, name='register')
]

