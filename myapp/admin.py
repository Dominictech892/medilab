from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(ward)
admin.site.register(Appointment)
admin.site.register(Contact1)
admin.site.register(Transaction)