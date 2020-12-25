from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import Visit
# Create your views here.
def index(request):
    return render(request,'app/home.html')
def donate(request):
    return render(request,'app/donate.html')
def contact(request):
    return render(request, 'app/contactus.html')
def aboutus(request):
    return render(request,'app/aboutus.html')
def gallery(request):
    return render(request,'app/gallery.html')
def visitus(request):
    return render(request,'app/visitus.html')
def visitusaction(request):
    print('hai')
    if request.method == 'POST':
        print('hello')
        obj  =  Visit()
        obj.name=request.POST.get('name')
        obj.phone=request.POST.get('phone')
        obj.email=request.POST.get('email')
        obj.time=request.POST.get('time')
        obj.date=request.POST.get('date')
        obj.purpose = request.POST.get('purpose')
        obj.save()
        print(obj.name)
        subject="welcome to Dharma's charity"
        message = f'Hai {obj.name} waiting for ur visit for your charity.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [obj.email,]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,'app/home.html')


def success(request):
    return render(request, 'app/success.html')
