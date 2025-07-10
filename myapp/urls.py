from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('starter/', views.starter, name='starter'),
    path('home/', views.home, name='index'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='service'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointments, name='appointments'),
    path('department/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete,),
    path('showcontact/', views.showcontact, name='showcontact'),

    #Mpesa API urls
    path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),



]





