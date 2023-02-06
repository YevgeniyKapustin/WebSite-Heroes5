from django import forms
from reports.models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['victory', 'myself', 'opponent', 'fraction_myself',
                  'fraction_opponent']
        widgets = {
            'myself': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent': forms.TextInput(attrs={'class': 'form-control'}),
            'fraction_myself': forms.Select(attrs={'class': 'form-control'}),
            'fraction_opponent': forms.Select(attrs={'class': 'form-control'})
        }
