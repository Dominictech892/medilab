from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib import messages
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

def contact(request):
   if request.method == 'POST':
       contacts =  Contact1(
           name=request.POST['name'],
           email=request.POST['email'],
           subject=request.POST['subject'],
           message=request.POST['message'],
       )
       contacts.save()
       messages.success(request, 'Your message has been sent. Thank you!')
       return redirect('/contact')
   else:
       messages.error(request, 'Please enter your message first.')
       return render(request, 'contact.html')


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
       messages.success(request, 'Your appointment has been submitted.')
       return redirect('/appointment')
   else:
       messages.error(request, 'Please enter your appointment first.')
       return render(request, 'appointments.html')
def departments(request):
    return render(request, 'departments.html')


def show(request):
    all = Appointment.objects.all()
    return render(request, 'show.html', {'all': all})

def delete(request,id):
    myappoint=Appointment.objects.get(id=id)
    myappoint.delete()
    return redirect('/show')

def showcontact(request):
    all = Contact1.objects.all()
    return render(request, 'showcontact.html', {'all': all})

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials!")
            return redirect('/home')  # Redirect back to login page

    return render(request, 'login.html')

