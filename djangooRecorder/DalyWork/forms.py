from django import forms
from . import models

class CreateInFormation(forms.ModelForm):
    class Meta:
        model = models.DalyWorkPost
        fields = ['client','workduty','AA','BB','CC','DD','EE','FF']
        widgets = {
            'client': forms.Textarea(attrs={'rows': 2}),
            'workduty': forms.Textarea(attrs={'rows': 3}),
        }