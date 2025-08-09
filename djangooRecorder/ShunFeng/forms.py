from django import forms
from . import models

class CreateInFormation(forms.ModelForm):
    class Meta:
        model = models.ShunFengPost
        fields = ['client','workduty','banner']
        widgets = {
            'client': forms.Textarea(attrs={'rows': 2}),
            'workduty': forms.Textarea(attrs={'rows': 3}),
        }