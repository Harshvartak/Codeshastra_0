from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person,ngo
from .smtptest import mailer,mailer1,mailer3,mailer4

def home(request):
     person=Person.objects
     ngo1=ngo.objects
     return render(request, 'needy/home.html',{'person':person,'ngos':ngo1})


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

            username=request.user.username
            mailer(Name,username)
            model=ngo.objects.all()
            ngli=[]

            for i in model:
                if i.location.lower() == person.location.lower():
                    mailer3(i.email)
                    ngli.append(i)
            person.save()
            return render(request, 'needy/thankyou.html',{'ngo':ngli})
        else:
            return render(request,'needy/create.html',{ 'error':'All fields are required' })

    else:
        return render(request,'needy/create.html')

def ngo_det(request,ng_id):
    ngo1 = get_object_or_404(ngo, pk = ng_id)
    return render(request,'ngo/ngdet.html', {'ngo':ngo1})

def donate(request, ng_id):
    ngo1 = get_object_or_404(ngo, pk = ng_id)
    dna = int(request.POST.get('don',False))
    ngo1.donations += dna
    ngo1.save()
    return render(request, 'ngo/donate.html',{'ngo':ngo1})

def thankyou(request, ng_id):
    ngo1 = get_object_or_404(ngo, pk = ng_id)
    em = request.POST.get('email',False)
    dna = int(request.POST.get('don',False))
    ngo1.donations += dna
    ngo1.save()
    mailer4(ngo1.name, em, dna)
    mailer1(em, ngo1.email, dna)
    return render(request, 'ngo/thankyou.html', {'ngo':ngo1})
