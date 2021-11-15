from django.db import models
from django.forms import ModelForm, TextInput, widgets
from .models import Cities


class addCity(ModelForm):
    class Meta:
        # inherit the "Cities" model in models.py
        model = Cities
        fields = ['cityName']
        # use widgets to add attributes of model fields
        widgets = {'cityName': TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Key a city Name'})}
