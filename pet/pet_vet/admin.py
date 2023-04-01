from django.contrib import admin
from .models import Appointment, Animals


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'date', 'phone_number', 'email']


@admin.register(Animals)
class Animals(admin.ModelAdmin):
    list_display = ['types']
