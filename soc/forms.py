from django import forms
from .models import Tema

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nazov', 'popis', 'konzultant', 'student', 'odbor', 'dostupnost', 'pocet_konzultacii']