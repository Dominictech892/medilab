from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('starter/', views.starter, name='starter'),
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='service'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointments, name='appointments'),
    path('department/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),


]





