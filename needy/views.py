from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person

def home(request):
     person=Person.objects
     return render(request, 'needy/home.html',{'person':person})


@login_required(login_url='/accounts/signup')
def create(request):
	if request.method=='POST':
		if request.POST['name'] and request.POST['description'] and request.POST['needs'] and request.FILES['image'] and request.POST['location']:
			person = Person()
			person.title=request.POST['name']
			person.body=request.POST['description']
			person.icon=request.POST['needs']
            person.icon=request.POST['location']
			person.image=request.FILES['image']
			person.save()
			return redirect('needy/thankyou.html')

		else:
			return render(request,'needy/create.html',{ 'error':'All fields are required' })

	else:
		return render(request,'needy/create.html')
