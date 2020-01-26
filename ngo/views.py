from django.shortcuts import render,get_object_or_404
from .models import ngo
from thankyoumail import mailer
from ngonotif import mailer1
# Create your views here.
def home(request):
    ngos = ngo.objects
    return render(request, 'ngo/home.html', {'ngos':ngos})
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
    mailer(ngo1.name, em, dna)
    mailer1(em, ngo1.email, dna )
    return render(request, 'ngo/thankyou.html', {'ngo':ngo1})
