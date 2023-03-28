from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'pet_vet/index.html')


def services(request):
    return render(request, 'pet_vet/services.html')


def shop(request):
    return render(request, 'pet_vet/shop.html')


def contacts(request):
    return render(request, 'pet_vet/contacts.html')


def about(request):
    return render(request, 'pet_vet/about.html')
