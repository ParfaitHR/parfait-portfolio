import django_filters
from django import forms
from .models import Job

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ['job_title','company_name','role','salary','location','experience']
        
        widgets = {
            'job_title' : forms.TextInput(attrs={'class':'form-control'}),
            'company_name' : forms.TextInput(attrs={'class':'form-control'}),
            'role' : forms.TextInput(attrs={'class':'form-control'}),
            'salary' : forms.NumberInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'experience' : forms.NumberInput(attrs={'class':'form-control'}),
            'jd' : forms.TextInput(attrs={'class':'form-control'}),
        }