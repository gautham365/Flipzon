from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable":"Gautham is great"
    }
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc,date=datetime.today())
        contact.save() 
        messages.success(request, 'Your response is Submitted.')   
    return render(request, 'contact.html')

def dotd(request):
    return render(request, 'dotd.html')

def refur(request):
    return render(request, 'refur.html')