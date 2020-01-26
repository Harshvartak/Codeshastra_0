from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .smtptest import mailer

def home(request):
     person=Person.objects
     return render(request, 'needy/home.html',{'person':person})


@login_required(login_url='/accounts/signup')
def create(request):
    if request.method=='POST':
        if request.POST['name'] and request.POST['description'] and request.POST['needs'] and request.FILES['image'] and request.POST['location']:
            person = Person()
            person.name=request.POST['name']
            Name=request.POST['name']
            person.description=request.POST['description']
            person.need=request.POST['needs']
            person.location=request.POST['location']
            person.image=request.FILES['image']
            person.save()
            username=request.user.username
            mailer(Name,username)
            return render(request, 'needy/thankyou.html')
        else:
            return render(request,'needy/create.html',{ 'error':'All fields are required' })

    else:
        return render(request,'needy/create.html')
