from django.shortcuts import render
from .models import Person

def home(request):
     person=Person.objects
     return render(request, 'needy/home.html',{'person':person})
