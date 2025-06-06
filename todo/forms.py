from django import forms
from .models import Task


class newTaskForm(forms.ModelForm):
    class Meta:
     model=Task
     fields=['title','description','completed']
     widgets = {
            'description': forms.Textarea(attrs={'rows': 3}), 
        }
     