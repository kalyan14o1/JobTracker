from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'position', 'application_date', 'status']
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
        }