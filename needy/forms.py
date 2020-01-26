from .models import Person
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','description','image','needs','location']
