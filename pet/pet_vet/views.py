from django.shortcuts import render, HttpResponse
from .models import Appointment, Animals


def index(request):
    return render(request, 'pet_vet/index.html')


def services(request):
    return render(request, 'pet_vet/services.html')


def appointment(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        email = request.POST.get('client_email')
        phone_number = request.POST.get('phone_number')
        pet_type = request.POST.get('pet_type')
        date = request.POST.get('date')
        item = Appointment(client_name=client_name, email=email, phone_number=phone_number, pet_type=pet_type,
                           date=date,)
        item.save()
        return render(request, 'pet_vet/doctor_appointment.html')
    else:
        animals = Animals.objects.all()
        context = {'animals': animals}
        return render(request, 'pet_vet/doctor_appointment.html', context=context)


def shop(request):
    return render(request, 'pet_vet/shop.html')


def contacts(request):
    return render(request, 'pet_vet/contacts.html')


def about(request):
    return render(request, 'pet_vet/about.html')
