from django.core import validators
from django import forms
from .models import Workoutmodel


class Workout(forms.ModelForm):
    class Meta:
        model= Workoutmodel
        fields = ['workout_type','duration','notes','date']
        widgets = {
            'workout_type': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }