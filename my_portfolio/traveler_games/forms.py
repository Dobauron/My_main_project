from .models import Player
from django import forms

class NameForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('name',)
