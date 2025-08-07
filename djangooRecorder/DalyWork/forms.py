from django import forms
from . import models

class CreateInFormation(forms.ModelForm):
    class Meta:
        model = models.DalyWorkPost
        fields = ['client','workduty','banner']
        widgets = {
            'workduty': forms.Textarea(attrs={'rows': 3}),
        }