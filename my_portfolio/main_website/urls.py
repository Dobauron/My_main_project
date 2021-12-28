from django.urls import path
from .views import index, Who_amI

urlpatterns=[
    path('', index, name="main_website"),
    path('Who_amI', Who_amI, name="Who_amI"),

]

