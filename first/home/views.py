from django.shortcuts import render , HttpResponse
from home.models import Contact , Registration
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request , 'index.html')
    # return HttpResponse('This is home page ')

def about(request):
    return render(request , 'about.html')
    # return HttpResponse('This is about page ')

def services(request):
    return render(request , 'services.html')
    # return HttpResponse('Design Develop Grow')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        place = request.POST.get('place')
        message = request.POST.get('message')
        contact = Contact(name=name , phone=phone , email=email , place=place , message=message , date=datetime.today() )
        contact.save()
        messages.success(request, 'Thank you!!! We will contact you shortly.')
    return render(request , 'contact.html')
    # return HttpResponse('How may I help you!!!')

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        address = request.POST.get('address')
        registration = Registration(name=name , email=email , gender=gender ,age=age , phone=phone , city=city , address=address , date=datetime.today())
        registration.save()
        messages.success(request , 'Your appointment has been booked!!!')



    return render( request ,'registration.html')
