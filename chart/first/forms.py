from django import forms
from .models import main

class second(forms.ModelForm):
    class Meta:
        model=main
        fields='__all__'
