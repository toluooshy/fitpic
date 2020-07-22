from django import forms
from django.forms import ModelForm

from .models import *

class ClothingForm(forms.ModelForm):

    class Meta:
        model = Clothing
        fields = '__all__'