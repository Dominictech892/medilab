from django.shortcuts import render, redirect
from myapp.models import *
# Create your views here.
def starter(request):
    return render(request, 'starter-page.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def appointments(request):
   if request.method == 'POST':
       myappointments =  Appointment(
           name=request.POST['name'],
           email=request.POST['email'],
           phone=request.POST['phone'],
           datetime=request.POST['date'],
           department=request.POST['department'],
           doctor=request.POST['doctor'],
           message=request.POST['message'],
       )
       myappointments.save()
       return redirect('/appointment')
   else:
       return render(request, 'appointments.html')

def departments(request):
    return render(request, 'departments.html')

