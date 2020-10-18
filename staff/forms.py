from django import forms
from .models import Crew as CrewModel

class Crew(forms.ModelForm):

    class Meta():
        model = CrewModel
        fields = ['username', 'email', 'salary']
