from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context= {
        "variable":"ABHI is great"
    }
   
    return render(request, 'index.html', context)
    #return HttpResponse("This is Homepage ")

def about(request):
    return render(request, 'about.html')
#    return HttpResponse("This is about page ")

def services(request):
    return render(request, 'services.html')
#    return HttpResponse("This is services page ")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=Email, phone=Phone, desc=desc,date= datetime.today())
        contact.save()
        messages.success(request, "Your massage has been sent....")

    return render(request, 'contact.html')
#    return HttpResponse("This is contact page ")