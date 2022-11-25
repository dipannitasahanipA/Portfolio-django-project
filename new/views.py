from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.massage = massage
        contact.save()
        return HttpResponse('<h1>Thanks for contact with us</h1>')
    return render(request,"contact.html")

def showdata(request):
    contact = Contact.objects.all()
    #for i in contact:
         #print(i.name)
    data = {'Contact':contact}
    return render(request,'showdata.html',data)


