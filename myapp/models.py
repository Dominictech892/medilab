from django.db import models

# Create your models here.
class patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    national_ID = models.CharField(max_length=20)
    medical_history = models.CharField(max_length=20)
    dob = models.DateField()
def __str__(self):
    return self.firstname + " " + self.lastname

class doctor(models.Model):
    Fullname = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    doctorId = models.IntegerField(max_length=20)
    age = models.IntegerField()
    department = models.CharField(max_length=20)

    def __str__(self):
       return self.Fullname + " " + self.department

#ward model

class ward(models.Model):
    ward_name = models.CharField(max_length=100)
    floor = models.IntegerField()
    department = models.CharField(max_length=20)
    Head_nurse = models.CharField(max_length=20)

    def __str__(self):
       return self.ward_name + " " + self.department

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact1(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
